from rest_framework import serializers
from .models import Country, Name, NameCountryProbability

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['code', 'name']


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ['name', 'request_count', 'last_accessed']


class NameCountryProbabilitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name.name')
    country = CountrySerializer()

    class Meta:
        model = NameCountryProbability
        fields = ['name', 'country', 'probability']
