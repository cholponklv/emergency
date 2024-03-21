from rest_framework import viewsets, filters
from django_filters import rest_framework as dj_filters

from .models import Tender
from .serializers import TenderSerializer
from.pagination import CustomPagination
from .filters import TenderFilter


class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = TenderFilter
    search_fields = ['name', 'description']