# serializers.py
from rest_framework import serializers
from .models import News

        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title_ru','title_kg','title_en', 'photo', 'created_at','target')

