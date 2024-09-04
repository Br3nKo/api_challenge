from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    """
    Country schema
    """
    class Meta:
        model = Country
        fields = ['name', 'countryCode', 'id', 'createdAt', 'groupId']
