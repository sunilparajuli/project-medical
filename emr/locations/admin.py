from django.contrib import admin

# Register your models here.
from .models import Country,Province, Municipality, District
admin.site.register([Country,Province,Municipality,District])