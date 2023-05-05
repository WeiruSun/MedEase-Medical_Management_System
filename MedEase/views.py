from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from MedEase.forms import PhysicianForm, NurseForm, PatientForm, AppointmentForm, RegistrationForm, VisitForm, \
    DiseaseForm, \
    TestForm, HaveTestForm, MedicationForm, PrescriptionForm, ProcedureForm, ProcedureAssignmentForm, DiagnosisForm
from MedEase.models import Physician, Nurse, Patient, Appointment, Registration, TimeSlot, Visit, Prescription, Test, \
    HaveTest, Diagnosis
from MedEase.utils import ObjectCreateMixin


class PhysicianList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/physician_list.html',
            {'physician_list': Physician.objects.all()}
        )


class PhysicianDetail(View):
    def get(self, request, pk):
        physician = get_object_or_404(
            Physician,
            pk=pk
        )
        appointment_list = physician.appointment.all()
        return render(
            request,
            'MedEase/physician_detail.html',
            {'physician': physician, 'appointment_list': appointment_list}
        )


class PhysicianCreate(ObjectCreateMixin, View):
    form_class = PhysicianForm
    template_name = 'MedEase/forms/physician_form.html'


class PhysicianUpdate(View):
    form_class = PhysicianForm
    template_name = 'MedEase/update_forms/physician_form_update.html'

    def get(self, request, pk):
        physician = get_object_or_404(
            Physician,
            pk=pk
        )
        bound_form = self.form_class(instance=physician)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'physician': physician}
        )

    def post(self, request, pk):
        physician = get_object_or_404(
            Physician,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=physician)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'instructor': physician,
            }
            return render(
                request,
                self.template_name,
                context
            )


class PhysicianDelete(View):
    def get(self, request, pk):
        physician = self.get_object(pk)
        appointments = physician.appointment.all()
        if appointments.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/physician_refuse_delete.html',
                {'physician': physician,
                 'appointments': appointments,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/physician_confirm_delete.html',
                {'instructor': physician}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Physician,
            pk=pk)

    def post(self, request, pk):
        physician = self.get_object(pk)
        physician.delete()
        return redirect('MedEase_physician_list_urlpattern')


class NurseList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/nurse_list.html',
            {'nurse_list': Nurse.objects.all()}
        )


class NurseDetail(View):
    def get(self, request, pk):
        nurse = get_object_or_404(
            Nurse,
            pk=pk
        )
        visit_list = nurse.visit.all()
        return render(
            request,
            'MedEase/nurse_detail.html',
            {'nurse': nurse, 'visit_list': visit_list}
        )


class NurseCreate(ObjectCreateMixin, View):
    form_class = NurseForm
    template_name = 'MedEase/forms/nurse_form.html'


class NurseUpdate(View):
    form_class = NurseForm
    template_name = 'MedEase/update_forms/nurse_form_update.html'

    def get(self, request, pk):
        nurse = get_object_or_404(
            Nurse,
            pk=pk
        )
        bound_form = self.form_class(instance=nurse)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'nurse': nurse}
        )

    def post(self, request, pk):
        nurse = get_object_or_404(
            Nurse,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=nurse)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'nurse': nurse,
            }
            return render(
                request,
                self.template_name,
                context
            )


class NurseDelete(View):
    def get(self, request, pk):
        nurse = self.get_object(pk)
        visits = nurse.visit.all()
        have_tests = nurse.have_test.all()
        if visits.count() > 0 or have_tests.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/nurse_refuse_delete.html',
                {'nurse': nurse,
                 'visits': visits,
                 'have_tests': have_tests,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/nurse_confirm_delete.html',
                {'nurse': nurse}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Nurse,
            pk=pk)

    def post(self, request, pk):
        nurse = self.get_object(pk)
        nurse.delete()
        return redirect('MedEase_nurse_list_urlpattern')


class PatientList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/patient_list.html',
            {'patient_list': Patient.objects.all()}
        )


class PatientDetail(View):
    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        registration_list = patient.registration.all()
        visit_list = []
        for registration in registration_list:
            visit = registration.visit
            visit_list.append(visit)

        return render(
            request,
            'MedEase/patient_detail.html',
            {'patient': patient,
             'registration_list': registration_list,
             'visit_list': visit_list, }
        )


class PatientCreate(ObjectCreateMixin, View):
    form_class = PatientForm
    template_name = 'MedEase/forms/patient_form.html'


class PatientUpdate(View):
    form_class = PatientForm
    template_name = 'MedEase/update_forms/patient_form_update.html'

    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        bound_form = self.form_class(instance=patient)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'patient': patient}
        )

    def post(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=patient)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'patient': patient,
            }
            return render(
                request,
                self.template_name,
                context
            )


class PatientDelete(View):
    def get(self, request, pk):
        patient = self.get_object(pk)
        registrations = patient.registration.all()

        if registrations.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/patient_refuse_delete.html',
                {'patient': patient,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/patient_confirm_delete.html',
                {'patient': patient}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Patient,
            pk=pk)

    def post(self, request, pk):
        patient = self.get_object(pk)
        patient.delete()
        return redirect('MedEase_patient_list_urlpattern')


class AppointmentList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/appointment_list.html',
            {'appointment_list': Appointment.objects.all()}
        )


class AppointmentDetail(View):
    def get(self, request, pk):
        appointment = get_object_or_404(
            Appointment,
            pk=pk
        )
        status = appointment.get_status()
        return render(
            request,
            'MedEase/appointment_detail.html',
            {'appointment': appointment, 'time_slot': appointment.time_slot,
             'physician': appointment.physician, 'status': status}
        )


class AppointmentCreate(ObjectCreateMixin, View):
    form_class = AppointmentForm
    template_name = 'MedEase/forms/appointment_form.html'


class AppointmentUpdate(View):
    form_class = AppointmentForm
    template_name = 'MedEase/update_forms/appointment_form_update.html'

    def get(self, request, pk):
        appointment = get_object_or_404(
            Appointment,
            pk=pk
        )
        bound_form = self.form_class(instance=appointment)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'appointment': appointment}
        )

    def post(self, request, pk):
        appointment = get_object_or_404(
            Appointment,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=appointment)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'appointment': appointment,
            }
            return render(
                request,
                self.template_name,
                context
            )


class AppointmentDelete(View):
    def get(self, request, pk):
        appointment = self.get_object(pk)
        registrations = appointment.registration.all()
        if registrations.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/appointment_refuse_delete.html',
                {'appointment': appointment,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/appointment_confirm_delete.html',
                {'appointment': appointment}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Appointment,
            pk=pk)

    def post(self, request, pk):
        appointment = self.get_object(pk)
        appointment.delete()
        return redirect('MedEase_appointment_list_urlpattern')


class RegistrationList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )


class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        return render(
            request,
            'MedEase/registration_detail.html',
            {'registration': registration, 'appointment': registration.appointment,
             'patient': registration.patient, 'physician': registration.appointment.physician}
        )


class RegistrationCreate(ObjectCreateMixin, View):
    form_class = RegistrationForm
    template_name = 'MedEase/forms/registration_form.html'


class RegistrationUpdate(View):
    form_class = RegistrationForm
    template_name = 'MedEase/update_forms/registration_form_update.html'

    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        bound_form = self.form_class(instance=registration)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'registration': registration}
        )

    def post(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=registration)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'registration': registration,
            }
            return render(
                request,
                self.template_name,
                context
            )


class RegistrationDelete(View):
    def get(self, request, pk):
        registration = self.get_object(pk)
        try:
            visit = registration.visit
        except ObjectDoesNotExist:
            visit = None

        # TODO: I feel like there would be a bug here because of the one-to-one relationship
        if not visit:
            print("well there is no visit")
            return render(
                request,
                'MedEase/delete_forms/registration_confirm_delete.html',
                {'registration': registration}
            )
        else:
            visit = registration.visit
            return render(
                request,
                'MedEase/delete_forms/registration_refuse_delete.html',
                {'registration': registration,
                 'visit': visit,
                 }
            )

    def get_object(self, pk):
        return get_object_or_404(
            Registration,
            pk=pk)

    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('MedEase_registration_list_urlpattern')


class VisitList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/visit_list.html',
            {'visit_list': Visit.objects.all()}
        )


class VisitDetail(View):
    def get(self, request, pk):
        visit = get_object_or_404(
            Visit,
            pk=pk
        )
        return render(
            request,
            'MedEase/visit_detail.html',
            {'visit': visit,
             'patient': visit.registration.patient,
             'nurse': visit.prep_nurse,
             'physician': visit.registration.appointment.physician,
             'appointment': visit.registration.appointment,
             'diagnoses': visit.diagnosis.all(),
             'testResults': visit.have_test.all(),
             'prescription_list': visit.prescription.all(),
             # 'procedure': visit.procedure.all(),
             },

        )


class VisitCreate(ObjectCreateMixin, View):
    form_class = VisitForm
    template_name = 'MedEase/forms/visit_form.html'


class VisitUpdate(View):
    form_class = VisitForm
    template_name = 'MedEase/update_forms/visit_form_update.html'

    def get(self, request, pk):
        visit = get_object_or_404(
            Visit,
            pk=pk
        )
        bound_form = self.form_class(instance=visit)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'visit': visit}
        )

    def post(self, request, pk):
        visit = get_object_or_404(
            Visit,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=visit)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'visit': visit,
            }
            return render(
                request,
                self.template_name,
                context
            )


class VisitDelete(View):
    def get(self, request, pk):
        visit = self.get_object(pk)
        diagnoses = visit.diagnosis.all()
        if diagnoses.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/visit_refuse_delete.html',
                {'visit': visit,
                 'diagnoses': diagnoses,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/visit_confirm_delete.html',
                {'visit': visit}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Visit,
            pk=pk)

    def post(self, request, pk):
        visit = self.get_object(pk)
        visit.delete()
        return redirect('MedEase_visit_list_urlpattern')


class HaveTestList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/have_test_list.html',
            {'have_test_list': HaveTest.objects.all()}
        )


class HaveTestDetail(View):
    def get(self, request, pk):
        have_test = get_object_or_404(
            HaveTest,
            pk=pk
        )
        return render(
            request,
            'MedEase/have_test_detail.html',
            {'have_test': have_test,
             'test': have_test.test, }
        )


class HaveTestCreate(ObjectCreateMixin, View):
    form_class = HaveTestForm
    template_name = 'MedEase/forms/have_test_form.html'


class HaveTestUpdate(View):
    form_class = HaveTestForm
    template_name = 'MedEase/update_forms/have_test_form_update.html'

    def get(self, request, pk):
        have_test = get_object_or_404(
            HaveTest,
            pk=pk
        )
        bound_form = self.form_class(instance=have_test)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'have_test': have_test}
        )

    def post(self, request, pk):
        have_test = get_object_or_404(
            HaveTest,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=have_test)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'have_test': have_test,
            }
            return render(
                request,
                self.template_name,
                context
            )


class DiagnosisList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/diagnosis_list.html',
            {'diagnosis_list': Diagnosis.objects.all()}
        )


class DiagnosisDetail(View):
    def get(self, request, pk):
        diagnosis = get_object_or_404(
            Diagnosis,
            pk=pk
        )
        return render(
            request,
            'MedEase/diagnosis_detail.html',
            {'diagnosis': diagnosis}
        )


class DiagnosisCreate(ObjectCreateMixin, View):
    form_class = DiagnosisForm
    template_name = 'MedEase/forms/diagnosis_form.html'


class DiagnosisUpdate(View):
    form_class = DiagnosisForm
    template_name = 'MedEase/update_forms/diagnosis_form_update.html'

    def get(self, request, pk):
        diagnosis = get_object_or_404(
            Diagnosis,
            pk=pk
        )
        bound_form = self.form_class(instance=diagnosis)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'diagnosis': diagnosis}
        )

    def post(self, request, pk):
        diagnosis = get_object_or_404(
            Diagnosis,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=diagnosis)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'diagnosis': diagnosis,
            }
            return render(
                request,
                self.template_name,
                context
            )


class PrescriptionList(View):
    def get(self, request):
        return render(
            request,
            'MedEase/prescription_list.html',
            {'prescription_list': Prescription.objects.all()}
        )


class PrescriptionDetail(View):
    def get(self, request, pk):
        prescription = get_object_or_404(
            Prescription,
            pk=pk
        )
        return render(
            request,
            'MedEase/prescription_detail.html',
            {'prescription': prescription}
        )


class PrescriptionCreate(ObjectCreateMixin, View):
    form_class = PrescriptionForm
    template_name = 'MedEase/forms/prescription_form.html'


class PrescriptionUpdate(View):
    form_class = PrescriptionForm
    template_name = 'MedEase/update_forms/prescription_form_update.html'

    def get(self, request, pk):
        prescription = get_object_or_404(
            Prescription,
            pk=pk
        )
        bound_form = self.form_class(instance=prescription)
        return render(
            request,
            self.template_name,
            {'form': bound_form, 'prescription': prescription}
        )

    def post(self, request, pk):
        prescription = get_object_or_404(
            Prescription,
            pk=pk
        )
        bound_form = self.form_class(request.POST, instance=prescription)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                'prescription': prescription,
            }
            return render(
                request,
                self.template_name,
                context
            )


class PrescriptionDelete(View):
    def get(self, request, pk):
        prescription = self.get_object(pk)
        medications = prescription.medications.all()
        if medications.count() > 0:
            return render(
                request,
                'MedEase/delete_forms/prescription_refuse_delete.html',
                {'prescription': prescription,
                 'medications': medications,
                 }
            )
        else:
            return render(
                request,
                'MedEase/delete_forms/prescription_confirm_delete.html',
                {'prescription': prescription}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Prescription,
            pk=pk)

    def post(self, request, pk):
        prescription = self.get_object(pk)
        prescription.delete()
        return redirect('MedEase_prescription_list_urlpattern')
