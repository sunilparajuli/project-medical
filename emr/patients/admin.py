from django.contrib import admin

# Register your models here.
from .models import Patient,PatientType,InsuranceProvider

admin.site.register([Patient,PatientType,InsuranceProvider])