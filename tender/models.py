from django.db import models
from project.models import Project

# Create your models here.


class Tender(models.Model):
    name = models.CharField(max_length=144)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()


class TenderDocument(models.Model):
    name = models.CharField(max_length=134)
    file = models.FileField()
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)