from rest_framework import serializers
from .models import Project, Photo, Document

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id','project', 'image', 'caption','created_at']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id','project', 'file', 'description','created_at']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            data['file'] = request.build_absolute_uri(instance.file.url)
        return data

class ProjectSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'photos', 'documents','created_at']
