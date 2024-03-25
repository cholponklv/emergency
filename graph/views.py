from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Graph1, Graph2, Graph3, Graph4
from .serializers import Graph1Serializer, Graph2Serializer,Graph4Serializer,Graph3Serializer

class Graph1ViewSet(viewsets.ModelViewSet):
    queryset = Graph1.objects.all()
    serializer_class = Graph1Serializer

class Graph2ViewSet(viewsets.ModelViewSet):
    queryset = Graph2.objects.all()
    serializer_class = Graph2Serializer


class Graph3ViewSet(viewsets.ModelViewSet):
    queryset = Graph3.objects.all()
    serializer_class = Graph3Serializer


class Graph4ViewSet(viewsets.ModelViewSet):
    queryset = Graph4.objects.all()
    serializer_class = Graph4Serializer

