from rest_framework import viewsets, filters
from django_filters import rest_framework as dj_filters

from .models import Tender,TenderResult
from .serializers import TenderSerializer,TenderResultSerializer
from.pagination import CustomPagination
from .filters import TenderFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = TenderFilter
    search_fields = ['name', 'description']

    @action(detail=True, methods=['post'])
    def create_result(self, request, pk=None):
        tender = self.get_object()
        serializer = TenderResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tender=tender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
