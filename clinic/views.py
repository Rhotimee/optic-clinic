from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor, Patient, Prescription, Book
from django.views.generic import TemplateView, ListView, DetailView, RedirectView


class IndexView(RedirectView):
    url = '/clinic'


class ClinicView(TemplateView):
    template_name = 'clinic/clinic.html'


class PrescriptionList(ListView):
    model = Prescription
    paginate_by = 10

    def get_queryset(self):
        return Prescription.objects.filter()[:100]


class DoctorList(ListView):
    model = Doctor
    paginate_by = 10

    def get_queryset(self):
        return Doctor.objects.filter()[:100]


class PatientList(ListView):
    model = Patient
    paginate_by = 10

    def get_queryset(self):
        return Patient.objects.filter()[:100]


class BookList(ListView):
    model = Book
    paginate_by = 10

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

