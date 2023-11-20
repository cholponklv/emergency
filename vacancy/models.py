from django.db import models
from project.models import Project

# Create your models here.


class Vacancy(models.Model):
    name = models.CharField(max_length=140)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)