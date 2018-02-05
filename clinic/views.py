from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView

from .models import Doctor, Patient, Prescription, Book
from .forms import PatientForm, DoctorForm, PrescriptionForm, BookForm


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


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'clinic/create-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # messages.success(self.request, 'Your task was created successfully. ')
        return super(PatientCreateView, self).form_valid(form)


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm

    template_name = 'clinic/create-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # messages.success(self.request, 'Your task was created successfully. ')
        return super(DoctorCreateView, self).form_valid(form)


class PrescriptionCreateView(LoginRequiredMixin, CreateView):
    model = Prescription
    form_class = PrescriptionForm

    template_name = 'clinic/create-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # messages.success(self.request, 'Your task was created successfully. ')
        return super(PrescriptionCreateView, self).form_valid(form)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'clinic/create-form.html'


