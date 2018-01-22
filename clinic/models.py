from django.shortcuts import reverse
from django.core.validators import RegexValidator
from django.db import models


class Patient(models.Model):
    gender_choices = (('male', 'male'),
                      ('female', 'female'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=7)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    occupation = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('clinic:patient-detail', args=[str(self.id)])


class Doctor(models.Model):
    gender_choices = (('male', 'male'),
                      ('female', 'female'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=7)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('clinic:doctor-detail', args=[str(self.id)])


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    left_sph = models.CharField(max_length=6, null=True, blank=True)
    left_cyl = models.CharField(max_length=6, null=True, blank=True)
    left_axis = models.CharField(max_length=6, null=True, blank=True)
    left_add = models.CharField(max_length=6, null=True, blank=True)
    right_sph = models.CharField(max_length=6, null=True, blank=True)
    right_cyl = models.CharField(max_length=6, null=True, blank=True)
    right_axis = models.CharField(max_length=6, null=True, blank=True)
    right_add = models.CharField(max_length=6, null=True, blank=True)
    photochromic = models.BooleanField(default=False)
    comment = models.TextField(max_length=100, null=True, blank=True)
    no_prescription = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.patient.last_name

    def get_absolute_url(self):
        return reverse('clinic:prescription-detail', args=[str(self.id)])


class Book(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('clinic:book-detail', args=[str(self.id)])