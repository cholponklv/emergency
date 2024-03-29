# views.py
from rest_framework import viewsets
from .models import Project, Photo,Document
from .serializers import ProjectSerializer, PhotoSerializer,DocumentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics

from.pagination import CustomPagination
from .filters import ProjectFilter, DocumentFilter
from rest_framework import filters
from django_filters import rest_framework as dj_filters
from django.db.models import Q
from news.models import  News
from news.serializers import  NewsSerializer
from tender.models import Tender
from tender.serializers import TenderSerializer
from landslide_points.models import Point
from landslide_points.serializers import PointSerializer
from rest_framework.views import APIView


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ProjectFilter
    search_fields = ['name', 'description']




class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, project_id):
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Проект не найден"}, status=status.HTTP_404_NOT_FOUND)
        request.data['project'] = project_id
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
    
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


    def create(self, request, project_id):
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Проект не найден"}, status=status.HTTP_404_NOT_FOUND)

        request.data['project'] = project_id
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
    
class AllPhotosView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class AllDocumentsView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = DocumentFilter
    search_fields = ['project', 'description']





class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)  
        if query:
            
            news = News.objects.filter(title__icontains=query)
            tenders = Tender.objects.filter(name__icontains=query)
            project = Project.objects.filter(name__icontains=query)
            document = Document.objects.filter(description__contains=query)
            news_serializer = NewsSerializer(news, many=True)
            tender_serializer = TenderSerializer(tenders, many=True)
            project_serializer = ProjectSerializer(project,many=True)
            document_serializer = DocumentSerializer(document,many=True)

            return Response({
                'news': news_serializer.data,
                'tenders': tender_serializer.data,
                'project':project_serializer.data,
                'document':document_serializer
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Пожалуйста, введите запрос для поиска.'}, status=status.HTTP_400_BAD_REQUEST)
