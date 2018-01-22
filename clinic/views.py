from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor, Patient, Prescription, Book
from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


class ClinicView(TemplateView):
    template_name = 'clinic/clinic.html'


class PrescriptionList(ListView):
    model = Prescription

    def get_queryset(self):
        return Prescription.objects.filter()[:100]


class DoctorList(ListView):
    model = Doctor

    def get_queryset(self):
        return Doctor.objects.filter()[:100]


class PatientList(ListView):
    model = Patient

    def get_queryset(self):
        return Patient.objects.filter()[:100]


class BookList(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter()[:100]


class BookDetail(DetailView):
    model = Book


class PrescriptionDetail(DetailView):
    model = Prescription


class PatientDetail(DetailView):
    model = Patient


class DoctorDetail(DetailView):
    model = Doctor

