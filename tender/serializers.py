from rest_framework import serializers
from .models import Tender, TenderDocument


class TendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ('id','name', 'project', 'description')





class TenderDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderDocument
        fields = ('id','name', 'file', 'tender', 'uploaded_at')

