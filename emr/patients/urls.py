from django.contrib import admin
from django.urls import path, include
from emr.patients.api.views import PatientView, PatientDetailView
from emr.patients.api.fhir import FhirPatientDetailApiView, FhirCoverageApiView, AttachmentUpload


urlpatterns = [
    path('detail/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    # URL pattern to access patient detail by ID, for instance: /patients/1/
]
app_name = 'patients'


urlpatterns += [
    path('', PatientView.as_view(), name="patient-view"),
    path('fhir/v4/patient/<str:insuranceid>/', FhirPatientDetailApiView.as_view(), name="patient-details"),
    path('fhir/v4/coverage/<str:insuranceid>/<str:date>/', FhirCoverageApiView.as_view(), name="patient-details"),
    path('fhir/v4/attachments/upload/', AttachmentUpload.as_view(), name="attachment-upload")
]