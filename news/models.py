from django.db import models
from project.models import Project
# Create your models here.
from django_ckeditor_5.fields import CKEditor5Field

class News(models.Model):
    title_ru = models.CharField(max_length=160,null=True,blank=True)
    title_kg = models.CharField(max_length=160,null=True,blank=True)
    title_en = models.CharField(max_length=160,null=True,blank=True)
    target_ru = CKEditor5Field('Ru Text', config_name='extends',null=True,blank=True)
    target_kg = CKEditor5Field('KG Text', config_name='extends',null=True,blank=True)
    target_en = CKEditor5Field('EN Text', config_name='extends',null=True,blank=True)
    photo = models.ImageField(upload_to='NewsPhoto',null = True,blank = True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title_ru
    





    