from rest_framework import generics
from emr.locations.models import Country, Province, District, Municipality
from .serializers import CountrySerializer, ProvinceSerializer, DistrictSerializer, MunicipalitySerializer

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProvinceList(generics.ListCreateAPIView):
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        country_id = self.kwargs.get('country_id')
        return Province.objects.filter(country_id=country_id)

class DistrictList(generics.ListCreateAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        province_id = self.kwargs.get('province_id')
        return District.objects.filter(province_id=province_id)

class MunicipalityList(generics.ListCreateAPIView):
    serializer_class = MunicipalitySerializer

    def get_queryset(self):
        district_id = self.kwargs.get('district_id')
        return Municipality.objects.filter(district_id=district_id)
