from django.shortcuts import render
from rest_framework import viewsets
from .models import News, Galery
from .serializers import NewsSerializer, GalerySerializer
# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class GaleryViewSet(viewsets.ModelViewSet):
    queryset = Galery.objects.all()
    serializer_class = GalerySerializer

