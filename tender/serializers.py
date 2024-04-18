from rest_framework import serializers
from .models import Tender, TenderResult,DocumentTender,DocumentResultTender

class TenderResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderResult
        fields = ('file','result_description_ru','result_description_kg','result_description_en',)

class TenderSerializer(serializers.ModelSerializer):
    result = TenderResultSerializer(required=False)

    class Meta:
        model = Tender
        fields = ('id', 'name_ru','name_kg','name_en', 'created_at', 'deadline', 'description_ru','description_kg','description_en',  'status', 'result')

class DocumentTenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTender
        fields = ['id','tender', 'file', 'description_ru','description_kg','description_en','created_at']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            data['file'] = request.build_absolute_uri(instance.file.url)
        return data

class DocumentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentResultTender
        fields = ['id','result', 'file', 'description_ru','description_kg','description_en','created_at']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            data['file'] = request.build_absolute_uri(instance.file.url)
        return data