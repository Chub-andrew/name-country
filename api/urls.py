from django.urls import path
from .views import NameCountryView, PopularNamesView

urlpatterns = [
    path('names/', NameCountryView.as_view(), name='name-country'),
    path('popular-names/', PopularNamesView.as_view(), name='popular-names'),
]
