from django.urls import path
from emr.locations.api import views
app_name="locations"
urlpatterns = [
    path('countries/', views.CountryList.as_view(), name='country-list'),
    path('countries/<int:country_id>/provinces/', views.ProvinceList.as_view(), name='province-list'),
    path('provinces/<int:province_id>/districts/', views.DistrictList.as_view(), name='district-list'),
    path('districts/<int:district_id>/municipalities/', views.MunicipalityList.as_view(), name='municipality-list'),
]
