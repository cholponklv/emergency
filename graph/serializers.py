from rest_framework import serializers
from .models import Graph1,Graph4,Graph3,Graph2

class Graph1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Graph1
        fields = ['id', 'month', 'value', 'type']

class Graph2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Graph2
        fields = ['id', 'type', 'x', 'y']

class Graph3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Graph3
        fields = ['id', 'month', 'value']

class Graph4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Graph4
        fields = ['id', 'name', 'created_at', 'costs']
