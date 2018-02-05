"""optical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import (
    PatientList,
    PrescriptionList,
    DoctorList,
    PatientDetail,
    DoctorDetail,
    PrescriptionDetail,
    ClinicView,
    BookList,
    BookDetail,
    DoctorCreateView, PrescriptionCreateView, PatientCreateView, BookCreateView
)

app_name = 'clinic'

urlpatterns = [
    path('', ClinicView.as_view(), name='dashboard'),
    path('patient/', PatientList.as_view(), name='patient-list'),
    path('prescription/', PrescriptionList.as_view(), name='prescription-list'),
    path('doctor/', DoctorList.as_view(), name='doctor-list'),
    path('book/', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('prescription/<int:pk>/', PrescriptionDetail.as_view(), name='prescription-detail'),
    path('create-doctor/', DoctorCreateView.as_view(), name='doctor-create'),
    path('create-prescription/', PrescriptionCreateView.as_view(), name='prescription-create'),
    path('create-patient/', PatientCreateView.as_view(), name='patient-create'),
    path('create-book/', BookCreateView.as_view(), name='book-create'),

]

