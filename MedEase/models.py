from django.db import models
from django.db.models import UniqueConstraint


class Department(models.Model):
    dept_ID = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '%s' % self.dept_name


class Physician(models.Model):
    physician_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Nurse(models.Model):
    physician_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Patient(models.Model):
    patient_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DOB = models.DateField()

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class TimeSlot(models.Model):
    slot_ID = models.AutoField(primary_key=True)
    sequence = models.IntegerField(unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '%s - %s' % (self.start_time, self.end_time)

    class Meta:
        ordering = ['sequence']
        constraints = [
            UniqueConstraint(fields=['start_time', 'end_time'], name='unique_timeslot')
        ]


class Appointment(models.Model):
    """the Appointment-Physician relationship:
    An appointment could have one and only one physician
    A physician could have many appointment """
    appointment_ID = models.AutoField(primary_key=True)
    physician = models.ForeignKey(Physician, related_name='appointment', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, related_name='appointment', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return '%s : %s, %s - %s, %s' % (
            self.physician, self.appointment_date, self.time_slot.start_time, self.time_slot.end_time,
            self.available)

    class Meta:
        ordering = ['appointment_date', 'time_slot__sequence']
        constraints = [
            UniqueConstraint(fields=['appointment_date', 'time_slot', 'physician'], name='unique_appointment')]


class Registration(models.Model):
    """the appointment-patient relationship:"""
    # todo: add a unique constraint
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.appointment.physician, self.patient)

    class Meta:
        ordering = ['appointment__appointment_date', 'appointment__time_slot']


class Visit(models.Model):
    """the Visit-Patient relationship:
        An visit could have one and only one patient
        A patient could have many Visit """
    visit_ID = models.AutoField(primary_key=True)
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s,  %s with physician: %s' % \
            (self.registration.appointment.time_slot.start_time, self.registration.patient.first_name,
             self.registration.patient.last_name,
             self.registration.appointment.physician.last_name)

    class Meta:
        ordering = ['registration__appointment__appointment_date', 'registration__appointment__time_slot__sequence']


class Disease(models.Model):
    disease_ID = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.disease_name


class Diagnosis(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.disease.disease_name)


class Test(models.Model):
    test_ID = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.test_name


class HaveTest(models.Model):
    test = models.OneToOneField(Test, on_delete=models.DO_NOTHING)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    test_date = models.DateField()

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.test.test_name)


class Medication(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ['name']
        constraints = [UniqueConstraint(fields=['name', 'brand'], name='unique_medication')]


class Prescription(models.Model):
    prescription_ID = models.AutoField(primary_key=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    date = models.DateField()
    dose = models.CharField(max_length=255)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.medication.name)


class Procedure(models.Model):
    procedure_ID = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.procedure_name


class ProcedureAssignment(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    operator = models.ForeignKey(Physician, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.operator.first_name)
