# views.py
from rest_framework import viewsets, filters
from django_filters import rest_framework as dj_filters

from .models import News
from .serializers import NewsSerializer
from.pagination import CustomPagination
from .filters import NewsFilter

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = NewsFilter
    search_fields = ['name', 'description']
