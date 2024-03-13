from rest_framework import serializers
from .models import Project, Photo, Document

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id','project', 'image', 'caption']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id','project', 'file', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'photos', 'documents']
