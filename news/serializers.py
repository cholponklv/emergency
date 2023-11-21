from rest_framework import serializers
from .models import Galery, News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','name', 'project', 'descrtiption', 'created_at')

class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = ('id', 'photo', 'project')

