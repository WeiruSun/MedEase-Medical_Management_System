from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Department(models.Model):
    dept_ID = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.dept_name


class Physician(models.Model):
    physician_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='physician')
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('MedEase_physician_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_physician_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_physician_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['department', 'last_name', 'first_name']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_physician')
        ]


class Nurse(models.Model):
    nurse_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('MedEase_nurse_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_nurse_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_nurse_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_nurse')
        ]


class Patient(models.Model):
    patient_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DOB = models.DateField()
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('MedEase_patient_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_patient_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_patient_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_patient')
        ]


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

    def __str__(self):
        if self.registration.all().count() == 0:
            status = 'available'
        else:
            status = 'registered'

        return '%s : %s, %s - %s' % (
            self.appointment_date,
            self.time_slot.start_time,
            self.time_slot.end_time,
            self.physician,)

    def get_status(self):
        if self.registration.all().count() == 0:
            status = 'available'
        else:
            status = 'not available'
        return status

    def get_absolute_url(self):
        return reverse('MedEase_appointment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_appointment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_appointment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['appointment_date', 'time_slot__sequence']
        constraints = [
            UniqueConstraint(fields=['appointment_date', 'time_slot', 'physician'], name='unique_appointment')]


class Registration(models.Model):
    """the appointment-patient relationship:"""
    # appointment = models.OneToOneField(Appointment, related_name="registration", on_delete=models.CASCADE)
    # patient = models.OneToOneField(Patient, related_name="registration", on_delete=models.CASCADE)
    registration_ID = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, related_name="registration", on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name="registration", on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.appointment, self.patient)

    def get_absolute_url(self):
        return reverse('MedEase_registration_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_registration_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_registration_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['appointment__appointment_date', 'appointment__time_slot']
        constraints = [
            UniqueConstraint(fields=['appointment'], name='unique_registration'),
        ]


class Visit(models.Model):
    """the Visit-Patient relationship:
        An visit could have one and only one patient
        A patient could have many Visit """
    visit_ID = models.AutoField(primary_key=True)
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='visit')
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name='visit')

    def __str__(self):
        return '%s %s,  %s with physician: %s' % \
            (self.registration.appointment.time_slot.start_time, self.registration.patient.first_name,
             self.registration.patient.last_name,
             self.registration.appointment.physician.last_name)

    def get_absolute_url(self):
        return reverse('MedEase_visit_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_visit_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_visit_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['registration__appointment__appointment_date', 'registration__appointment__time_slot__sequence']
        constraints = [
            UniqueConstraint(fields=['registration', 'prep_nurse'], name='unique_visit')
        ]


class Disease(models.Model):
    disease_ID = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.disease_name

    def get_absolute_url(self):
        return reverse('MedEase_disease_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_disease_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Diagnosis(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='diagnosis')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.disease.disease_name)

    def get_absolute_url(self):
        return reverse('MedEase_diagnosis_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_diagnosis_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_diagnosis_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Test(models.Model):
    test_ID = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.test_name

    def get_absolute_url(self):
        return reverse('MedEase_test_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_test_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class HaveTest(models.Model):
    have_test_ID = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING, related_name='have_test')
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='have_test')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='have_test')
    test_date = models.DateField()
    # todo: add test result, test_result should be a choice field
    test_result = models.CharField(max_length=255)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.test.test_name)

    def get_absolute_url(self):
        return reverse('MedEase_haveTest_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_haveTest_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_haveTest_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['test_date']
        constraints = [UniqueConstraint(fields=['test', 'visit'], name='unique_havetest')]


class Medication(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('MedEase_medication_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_medication_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['name']
        constraints = [UniqueConstraint(fields=['name', 'brand'], name='unique_medication')]


class Prescription(models.Model):
    prescription_ID = models.AutoField(primary_key=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='prescription')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='prescription')
    date = models.DateField()
    dose = models.CharField(max_length=255)

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.medication.name)

    def get_absolute_url(self):
        return reverse('MedEase_prescription_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_prescription_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_prescription_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class Procedure(models.Model):
    procedure_ID = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.procedure_name

    def get_absolute_url(self):
        return reverse('MedEase_procedure_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_procedure_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )


class ProcedureAssignment(models.Model):
    procedure_assignment_ID = models.AutoField(primary_key=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='procedure_assignment')
    operator = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='procedure_assignment')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, related_name='procedure_assignment')

    def __str__(self):
        return '%s, %s' % (self.visit.registration.patient.first_name, self.operator.first_name)

    def get_absolute_url(self):
        return reverse('MedEase_procedureassignment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('MedEase_procedureassignment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('MedEase_procedureassignment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )
