from rest_framework import serializers
from .models import Project, Team, MemberTeam



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'country', 'photo', 'phone')


class MemberTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTeam
        fields = ('id', 'team', 'name')



class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name', 'status', 'team','longitude','latitude', 'description', 'owner', 'budget', 'deadline', 'start_at', 'color')





