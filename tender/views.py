from rest_framework import viewsets, filters
from django_filters import rest_framework as dj_filters

from .models import Tender,TenderResult
from .serializers import TenderSerializer,TenderResultSerializer
from.pagination import CustomPagination
from .filters import TenderFilter
from rest_framework import generics

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = TenderFilter
    search_fields = ['name', 'description']

class TenderResultListView(generics.ListAPIView):
    serializer_class = TenderResultSerializer

    def get_queryset(self):
        tender_id = self.kwargs['id']
        return TenderResult.objects.filter(tender_id=tender_id)