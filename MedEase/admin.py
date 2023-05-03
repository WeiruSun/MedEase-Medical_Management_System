from django.contrib import admin

from .models import Department, Physician, Nurse, Patient, Appointment,Registration, Visit, Disease, Diagnosis, Test, HaveTest, \
    TimeSlot, Medication, Prescription, Procedure, ProcedureAssignment

# Register your models here.
admin.site.register(Department)
admin.site.register(Physician)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Visit)
admin.site.register(Disease)
admin.site.register(Diagnosis)
admin.site.register(Test)
admin.site.register(HaveTest)
admin.site.register(TimeSlot)
admin.site.register(Medication)
admin.site.register(Prescription)
admin.site.register(Procedure)
admin.site.register(ProcedureAssignment)
admin.site.register(Registration)
