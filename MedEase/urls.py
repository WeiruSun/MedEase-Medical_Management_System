from django.urls import path
from MedEase.views import (
    PhysicianList, NurseList, PatientList, AppointmentList, RegistrationList,
    PhysicianDetail, NurseDetail, PatientDetail, AppointmentDetail, RegistrationDetail, VisitList, VisitDetail,
    PhysicianCreate, NurseCreate, PatientCreate, AppointmentCreate, RegistrationCreate, VisitCreate,
    PhysicianUpdate, NurseUpdate, PatientUpdate, AppointmentUpdate, RegistrationUpdate, VisitUpdate,
    PhysicianDelete, NurseDelete, HaveTestCreate, HaveTestList, PatientDelete, AppointmentDelete, RegistrationDelete,
    VisitDelete,
)

urlpatterns = [
    path("physician/", PhysicianList.as_view(), name="MedEase_physician_list_urlpattern"),
    path("physician/<int:pk>/", PhysicianDetail.as_view(), name="MedEase_physician_detail_urlpattern"),
    path("nurse/", NurseList.as_view(), name="MedEase_nurse_list_urlpattern"),
    path("nurse/<int:pk>/", NurseDetail.as_view(), name="MedEase_nurse_detail_urlpattern"),
    path("patient/", PatientList.as_view(), name="MedEase_patient_list_urlpattern"),
    path("patient/<int:pk>/", PatientDetail.as_view(), name="MedEase_patient_detail_urlpattern"),
    path("appointment/", AppointmentList.as_view(), name="MedEase_appointment_list_urlpattern"),
    path("appointment/<int:pk>/", AppointmentDetail.as_view(), name="MedEase_appointment_detail_urlpattern"),
    path("registration/", RegistrationList.as_view(), name="MedEase_registration_list_urlpattern"),
    path("registration/<int:pk>/", RegistrationDetail.as_view(), name="MedEase_registration_detail_urlpattern"),
    path("visit/", VisitList.as_view(), name="MedEase_visit_list_urlpattern"),
    path("visit/<int:pk>/", VisitDetail.as_view(), name="MedEase_visit_detail_urlpattern"),
    path("haveTest/", HaveTestList.as_view(), name="MedEase_haveTest_list_urlpattern"),


    # create
    path("physician/create/", PhysicianCreate.as_view(), name="MedEase_physician_create_urlpattern"),
    path("nurse/create/", NurseCreate.as_view(), name="MedEase_nurse_create_urlpattern"),
    path("patient/create/", PatientCreate.as_view(), name="MedEase_patient_create_urlpattern"),
    path("appointment/create/", AppointmentCreate.as_view(), name="MedEase_appointment_create_urlpattern"),
    path("registration/create/", RegistrationCreate.as_view(), name="MedEase_registration_create_urlpattern"),
    path("visit/create/", VisitCreate.as_view(), name="MedEase_visit_create_urlpattern"),
    # path("test/create/", TestCreate.as_view(), name="MedEase_test_create_urlpattern"),
    path("haveTest/create/", HaveTestCreate.as_view(), name="MedEase_haveTest_create_urlpattern"),
    # path("prescription/create/", PrescriptionCreate.as_view(), name="MedEase_prescription_create_urlpattern"),
    # path("medication/create/", MedicationCreate.as_view(), name="MedEase_medication_create_urlpattern"),
    # path("procedure/create/", ProcedureCreate.as_view(), name="MedEase_procedure_create_urlpattern"),
    # path("procedureAssignment/create/", ProcedureAssignmentCreate.as_view(), name="MedEase_procedureAssignment_create_urlpattern"
    # path("diagnosis/create/", DiagnosisCreate.as_view(), name="MedEase_diagnosis_create_urlpattern"),
    # path("disease/create/", DiseaseCreate.as_view(), name="MedEase_disease_create_urlpattern"),

    # update
    path("physician/<int:pk>/update/", PhysicianUpdate.as_view(), name="MedEase_physician_update_urlpattern"),
    path("nurse/<int:pk>/update/", NurseUpdate.as_view(), name="MedEase_nurse_update_urlpattern"),
    path("patient/<int:pk>/update/", PatientUpdate.as_view(), name="MedEase_patient_update_urlpattern"),
    path("appointment/<int:pk>/update/", AppointmentUpdate.as_view(), name="MedEase_appointment_update_urlpattern"),
    path("registration/<int:pk>/update/", RegistrationUpdate.as_view(), name="MedEase_registration_update_urlpattern"),
    path("visit/<int:pk>/update/", VisitUpdate.as_view(), name="MedEase_visit_update_urlpattern"),
    # # path("test/<int:pk>/update/", TestUpdate.as_view(), name="MedEase_test_update_urlpattern"),
    # path("haveTest/<int:pk>/update/", HaveTestUpdate.as_view(), name="MedEase_haveTest_update_urlpattern"),
    # path("prescription/<int:pk>/update/", PrescriptionUpdate.as_view(), name="MedEase_prescription_update_urlpattern"),
    # path("medication/<int:pk>/update/", MedicationUpdate.as_view(), name="MedEase_medication_update_urlpattern"),
    # path("procedure/<int:pk>/update/", ProcedureUpdate.as_view(), name="MedEase_procedure_update_urlpattern"),
    # path("procedureAssignment/<int:pk>/update/", ProcedureAssignmentUpdate.as_view(), name="MedEase_procedureAssignment_update_urlpattern"),
    # path("diagnosis/<int:pk>/update/", DiagnosisUpdate.as_view(), name="MedEase_diagnosis_update_urlpattern"),
    # path("disease/<int:pk>/update/", DiseaseUpdate.as_view(), name="MedEase_disease_update_urlpattern"),


    #delete
    path("physician/<int:pk>/delete/", PhysicianDelete.as_view(), name="MedEase_physician_delete_urlpattern"),
    path("nurse/<int:pk>/delete/", NurseDelete.as_view(), name="MedEase_nurse_delete_urlpattern"),
    path("patient/<int:pk>/delete/", PatientDelete.as_view(), name="MedEase_patient_delete_urlpattern"),
    path("appointment/<int:pk>/delete/", AppointmentDelete.as_view(), name="MedEase_appointment_delete_urlpattern"),
    path("registration/<int:pk>/delete/", RegistrationDelete.as_view(), name="MedEase_registration_delete_urlpattern"),
    path("visit/<int:pk>/delete/", VisitDelete.as_view(), name="MedEase_visit_delete_urlpattern"),
    # # path("test/<int:pk>/delete/", TestDelete.as_view(), name="MedEase_test_delete_urlpattern"),
    # path("haveTest/<int:pk>/delete/", HaveTestDelete.as_view(), name="MedEase_haveTest_delete_urlpattern"),
    # path("prescription/<int:pk>/delete/", PrescriptionDelete.as_view(), name="MedEase_prescription_delete_urlpattern"),
    # path("medication/<int:pk>/delete/", MedicationDelete.as_view(), name="MedEase_medication_delete_urlpattern"),
    # path("procedure/<int:pk>/delete/", ProcedureDelete.as_view(), name="MedEase_procedure_delete_urlpattern"),
    # path("procedureAssignment/<int:pk>/delete/", ProcedureAssignmentDelete.as_view(), name="MedEase_procedureAssignment_delete_urlpattern"),
    # path("diagnosis/<int:pk>/delete/", DiagnosisDelete.as_view(), name="MedEase_diagnosis_delete_urlpattern"),
    # path("disease/<int:pk>/delete/", DiseaseDelete.as_view(), name="MedEase_disease_delete_urlpattern"),


]
