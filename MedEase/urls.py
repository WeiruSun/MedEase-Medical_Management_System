from django.urls import path
from MedEase.views import (
    physician_list_view,
    nurse_list_view,
    patient_list_view,
    appointment_list_view,
    registration_list_view,)

urlpatterns = [
    path("physician/", physician_list_view),
    path("nurse/", nurse_list_view),
    path("patient/", patient_list_view),
    path("appointment/", appointment_list_view),
    path("registration/", registration_list_view),

]
