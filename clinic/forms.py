from django import forms
from .models import Patient, Doctor, Prescription, Book


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'other_name', 'email', 'gender', 'dob', 'age', 'phone_number', 'occupation', 'address')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'other_name', 'email', 'gender', 'dob', 'age', 'phone_number', 'address')


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('patient', 'doctor', 'left_sph', 'left_cyl', 'left_axis', 'left_add', 'right_sph', 'right_cyl',
                  'right_axis', 'right_add', 'photochromic', 'no_prescription', 'comment', 'date')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('full_name', 'email', 'phone_number', 'date')