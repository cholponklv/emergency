from rest_framework import viewsets, filters
from django_filters import rest_framework as dj_filters

from .models import Tender,TenderResult,DocumentTender,DocumentResultTender
from .serializers import TenderSerializer,TenderResultSerializer,DocumentTenderSerializer,DocumentResultSerializer
from.pagination import CustomPagination
from .filters import TenderFilter
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = TenderFilter
    search_fields = ['name_ru','name_kg','name_en','description_ru','description_kg','description_en']

class TenderResultListView(generics.ListAPIView):
    serializer_class = TenderResultSerializer

    def get_queryset(self):
        tender_id = self.kwargs['id']
        return TenderResult.objects.filter(tender_id=tender_id)
    
class DocumentTenderViewSet(viewsets.ModelViewSet):
    queryset = DocumentTender.objects.all()
    serializer_class = DocumentTenderSerializer

    def create(self, request, tender_id):
        try:
            tender = tender.objects.get(pk=tender_id)
        except Tender.DoesNotExist:
            return Response({"error": "Тендер не найден"}, status=status.HTTP_404_NOT_FOUND)

        request.data['tender'] = tender_id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AllDocumentsTendersView(generics.ListAPIView):
    queryset = DocumentTender.objects.all()
    serializer_class = DocumentTenderSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['tender', 'description_ru','description_kg','description_en']

class DocumentResultTenderViewSet(viewsets.ModelViewSet):
    queryset = DocumentResultTender.objects.all()
    serializer_class = DocumentTenderSerializer

    def create(self, request, result_id):
        try:
            result = result.objects.get(pk=result_id)
        except DocumentResultTender.DoesNotExist:
            return Response({"error": "Итог не найден"}, status=status.HTTP_404_NOT_FOUND)

        request.data['result'] = result_id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AllDocumentsResultTendersView(generics.ListAPIView):
    queryset = DocumentResultTender.objects.all()
    serializer_class = DocumentResultSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['tender', 'description_ru','description_kg','description_en']