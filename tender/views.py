from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets
from .models import Tender, TenderDocument
from .serializers import TenderDocumentsSerializer, TendersSerializer
# Create your views here.


class TendersViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TendersSerializer




class TenderDocumentsViewSet(viewsets.ModelViewSet):
    queryset = TenderDocument.objects.all()
    serializer_class = TenderDocumentsSerializer

