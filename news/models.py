from django.db import models
from project.models import Project
# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=160)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    descrtiption = models.TextField()
    photo = models.ManyToManyField('Galery', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)




class Galery(models.Model):
    photo = models.ImageField(upload_to='Galery')

    