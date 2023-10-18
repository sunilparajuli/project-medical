from django.db import models

from emr.utils.time_stamp_model import TimestampedModel
# Create your models here.
class Country(TimestampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, unique=True)
    
    def __str__(self):
        return f"{self.name}"


class Province(TimestampedModel):
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country.name} -> {self.name}"

class District(TimestampedModel):
    name=models.CharField(max_length=100)
    province=models.ForeignKey(Province,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.province.country.name} -> {self.province.name} -> {self.name}"

class Municipality(TimestampedModel):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.district.province.country.name} -> {self.district.province.name} -> {self.district.name} -> {self.name}"
    
