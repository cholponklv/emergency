from django.db import models
from project.models import Project

# Create your models here.


class Tender(models.Model):
    name = models.CharField(max_length=144)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    description = models.TextField()
    


