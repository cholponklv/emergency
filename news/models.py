from django.db import models
from project.models import Project
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=160)
    quote = models.TextField()
    base_quote = models.TextField()
    photo = models.ImageField(upload_to='NewsPhoto',null = True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Target(models.Model):
    news = models.ForeignKey(News, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name




    