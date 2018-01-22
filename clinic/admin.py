from django.contrib import admin
from .models import Patient, Doctor, Prescription, Book


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number')


class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number')


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'left_sph', 'left_cyl', 'left_axis', 'left_add', 'right_sph', 'right_cyl', 'right_axis', 'right_add']
    list_filter = ('doctor', 'patient', 'date')
    fields = [('patient', 'doctor'), ('left_sph', 'left_cyl', 'left_axis', 'left_add'),
              ('right_sph', 'right_cyl', 'right_axis', 'right_add'),
              ('photochromic', 'no_prescription'),
              'date']


class BookAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'email', 'message', 'date', 'timestamp']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Book, BookAdmin)
