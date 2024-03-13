from django.db import models
from project.models import Project
# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(null = True,blank = True)
    photo = models.ImageField(upload_to='NewsPhoto')
    created_at = models.DateTimeField(auto_now_add=True)





    