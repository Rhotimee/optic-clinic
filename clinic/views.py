from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor, Patient, Prescription
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index.html'


class PrescriptionList(ListView):
    model = Prescription

    def get_queryset(self):
        return Prescription.objects.filter()[:50]


class DoctorList(ListView):
    model = Doctor

    def get_queryset(self):
        return Doctor.objects.filter()[:10]


class PatientList(ListView):
    model = Patient

    def get_queryset(self):
        return Patient.objects.filter()[:50]
