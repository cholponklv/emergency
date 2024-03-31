from rest_framework import serializers
from .models import Tender, TenderResult

class TenderResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderResult
        fields = ('result_description',)

class TenderSerializer(serializers.ModelSerializer):
    result = TenderResultSerializer(required=False)

    class Meta:
        model = Tender
        fields = ('id', 'name', 'created_at', 'deadline', 'description', 'status', 'result')
