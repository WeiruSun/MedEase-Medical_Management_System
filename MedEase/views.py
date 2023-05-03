from django.shortcuts import render

from MedEase.models import (Physician, Nurse, Patient, Appointment, Registration)


def physician_list_view(request):
    physician_list = Physician.objects.all()
    # physician_list = Physician.objects.none()
    return render(request, 'MedEase/physician_list.html', {'physician_list': physician_list})


def nurse_list_view(request):
    nurse_list = Nurse.objects.all()
    # nurse_list = Nurse.objects.none()
    return render(request, 'MedEase/nurse_list.html', {'nurse_list': nurse_list})


def patient_list_view(request):
    patient_list = Patient.objects.all()
    # patient_list = Patient.objects.none()
    return render(request, 'MedEase/patient_list.html', {'patient_list': patient_list})


def appointment_list_view(request):
    appointment_list = Appointment.objects.all()
    # appointment_list = Appointment.objects.none()
    return render(request, 'MedEase/appointment_list.html', {'appointment_list': appointment_list})


def registration_list_view(request):
    registration_list = Registration.objects.all()
    # registration_list = Registration.objects.none()
    return render(request, 'MedEase/registration_list.html', {'registration_list': registration_list})
