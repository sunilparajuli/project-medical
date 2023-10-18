from django.db import models
from emr.utils.time_stamp_model import TimestampedModel
from emr.locations.models import Country,Province,District,Municipality
# Create your models here.
class PatientType(TimestampedModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.name

class InsuranceProvider(TimestampedModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    code = models.CharField(unique=True)
    def __str__(self):
        return self.name
class Patient(TimestampedModel):
    identifier = models.CharField(max_length=50, null=True,)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True,)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='patients/photo', null=True, blank=True)
    insurance = models.ForeignKey(InsuranceProvider, on_delete=models.SET_NULL, null=True, blank=True)
    patient_type = models.ForeignKey(PatientType, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.identifier}"



