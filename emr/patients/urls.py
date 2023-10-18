from django.contrib import admin
from django.urls import path, include
from emr.patients.api.views import PatientView

app_name = 'patients'


urlpatterns = [
    path('', PatientView.as_view(), name="patient-view"),
]