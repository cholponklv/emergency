from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbacksSerializer
# Create your views here.


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbacksSerializer

