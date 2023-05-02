from django.db import models


class Department(models.Model):
    dept_ID = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)


class Physician(models.Model):
    physician_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)


class Nurse(models.Model):
    physician_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Patient(models.Model):
    ssn = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DOB = models.DateField()


class TimeSlot(models.Model):
    slot_ID = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    """the Appointment-Physician relationship:
    An appointment could have one and only one physician
    A physician could have many appointment """
    appointment_ID = models.AutoField(primary_key=True)
    physician_ID = models.ForeignKey(Physician, related_name='appointment', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, related_name='appointment', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


class Visit(models.Model):
    """the Visit-Patient relationship:
        An visit could have one and only one patient
        A patient could have many Visit """
    visit_ID = models.AutoField(primary_key=True)
    appointment_ID = models.ForeignKey(Appointment, related_name='visit', on_delete=models.CASCADE)
    patient_ID = models.OneToOneField(Patient, on_delete=models.CASCADE)
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)


class Disease(models.Model):
    disease_ID = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255)


class Diagnosis(models.Model):
    visit_ID = models.ForeignKey(Visit, on_delete=models.CASCADE)
    disease_ID = models.ForeignKey(Disease, on_delete=models.CASCADE)


class Test(models.Model):
    test_ID = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class HaveTest(models.Model):
    test_ID = models.AutoField(primary_key=True)
    visit_ID = models.ForeignKey(Visit, on_delete=models.CASCADE)
    nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)


class Medication(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Prescription(models.Model):
    prescription_ID = models.AutoField(primary_key=True)
    visit_ID = models.ForeignKey(Visit, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    date = models.DateField()
    dose = models.CharField(max_length=255)


class Procedure(models.Model):
    procedure_ID = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class ProcedureAssignment(models.Model):
    visit_ID = models.ForeignKey(Visit, on_delete=models.CASCADE)
    operator = models.ForeignKey(Physician, on_delete=models.CASCADE)
