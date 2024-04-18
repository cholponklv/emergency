# serializers.py
from rest_framework import serializers
from .models import Point

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('id', 'name_ru','name_kg','name_en', 'status', 'longitude', 'latitude', 'location', 'speed','temperature','finished','depth')
