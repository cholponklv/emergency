import django_filters
from .models import Project, Document

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = []
        ordering_fields = ['name']



class DocumentFilter(django_filters.FilterSet):
    project = django_filters.ModelChoiceFilter(field_name='project', queryset=Project.objects.all())
    
    class Meta:
        model = Document
        fields = ['project'] 
        ordering_fields = ['name']
