from django import forms

from MedEase.models import (
    Physician,
    Nurse,
    Patient,
    Appointment,
    Registration,
    Disease,
    Test,
    HaveTest,
    Medication,
    Prescription,
    Procedure,
    ProcedureAssignment, Visit, Diagnosis,
)


class PhysicianForm(forms.ModelForm):
    class Meta:
        model = Physician
        fields = '__all__'

    def clear_first_name(self):
        first_name = self.cleaned_data['first_name'].strip()
        if first_name == '':
            raise forms.ValidationError('First name cannot be blank')
        return first_name

    def clear_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        if last_name == '':
            raise forms.ValidationError('Last name cannot be blank')
        return last_name


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'

    def clear_first_name(self):
        first_name = self.cleaned_data['first_name'].strip()
        if first_name == '':
            raise forms.ValidationError('First name cannot be blank')
        return first_name

    def clear_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        if last_name == '':
            raise forms.ValidationError('Last name cannot be blank')
        return last_name


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clear_first_name(self):
        first_name = self.cleaned_data['first_name'].strip()
        if first_name == '':
            raise forms.ValidationError('First name cannot be blank')
        return first_name

    def clear_last_name(self):
        last_name = self.cleaned_data['last_name'].strip()
        if last_name == '':
            raise forms.ValidationError('Last name cannot be blank')
        return last_name

    def clean_DOB(self):
        DOB = self.cleaned_data['DOB']
        if DOB == '':
            raise forms.ValidationError('Date of Birth cannot be blank')
        return DOB


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date == '':
            raise forms.ValidationError('Appointment date cannot be blank')
        return appointment_date


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def clean_registration_date(self):
        registration_date = self.cleaned_data['registration_date']
        if registration_date == '':
            raise forms.ValidationError('Registration date cannot be blank')
        return registration_date


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'

    def clean_disease_name(self):
        disease_name = self.cleaned_data['disease_name'].strip()
        if disease_name == '':
            raise forms.ValidationError('Disease cannot be blank')
        return disease_name


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

    def clean_test(self):
        test_name = self.cleaned_data['test_name'].strip()
        if test_name == '':
            raise forms.ValidationError('Test cannot be blank')
        return test_name

    def clean_price(self):
        price = self.cleaned_data['price'].strip()
        if price == '':
            raise forms.ValidationError('Price cannot be blank')
        return price


class HaveTestForm(forms.ModelForm):
    class Meta:
        model = HaveTest
        fields = '__all__'


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'

    def clean_medication_name(self):
        name = self.cleaned_data['name'].strip()
        if name == '':
            raise forms.ValidationError('Medication cannot be blank')
        return name

    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if brand == '':
            raise forms.ValidationError('Brand cannot be blank')
        return brand

    def clean_price(self):
        price = self.cleaned_data['price'].strip()
        if price == '':
            raise forms.ValidationError('Price cannot be blank')
        return price


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

    def clean_prescription_dose(self):
        dose = self.cleaned_data['dose'].strip()
        if dose == '':
            raise forms.ValidationError('Prescription date cannot be blank')
        return dose


class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'

    def clean_procedure_name(self):
        procedure_name = self.cleaned_data['procedure_name'].strip()
        if procedure_name == '':
            raise forms.ValidationError('Procedure name cannot be blank')
        return procedure_name

    def clean_price(self):
        cost = self.cleaned_data['cost'].strip()
        if cost == '':
            raise forms.ValidationError('Price cannot be blank')
        return cost


class ProcedureAssignmentForm(forms.ModelForm):
    class Meta:
        model = ProcedureAssignment
        fields = '__all__'
