# serializers.py
from rest_framework import serializers
from .models import News,Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name','description']
        
class NewsSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = ('id', 'title','quote','base_quote', 'photo', 'created_at','targets')

