from django.contrib import admin
from .models import Country, Name, NameCountryProbability

admin.site.register(Country)
admin.site.register(Name)
admin.site.register(NameCountryProbability)
