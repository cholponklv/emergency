from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Project, MemberTeam, Team,Photo
from .serializers import ProjectsSerializer, MemberTeamSerializer, TeamSerializer,PhotoSerializer
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer




class MemberTeamViewSet(viewsets.ModelViewSet):
    queryset = MemberTeam.objects.all()
    serializer_class = MemberTeamSerializer
    