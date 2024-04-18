from django.db import models
from project.models import Project
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Tender(models.Model):
    TYPE_CHOICES = [
        ('progress', 'В процессе'),
        ('finished', 'Закончен'),
    ]
    name_ru = models.CharField(max_length=256,null=True,blank=True)
    name_kg = models.CharField(max_length=256,null=True,blank=True)
    name_en = models.CharField(max_length=256,null=True,blank=True)
    created_at = models.DateField()
    deadline = models.DateField()
    description_ru = CKEditor5Field('ru Description', config_name='extends',null=True,blank=True)
    description_kg = CKEditor5Field('kg Description', config_name='extends',null=True,blank=True)
    description_en = CKEditor5Field('en Description', config_name='extends',null=True,blank=True)
    status = models.CharField(max_length=200, choices=TYPE_CHOICES)

class TenderResult(models.Model):
    tender = models.OneToOneField('Tender', on_delete=models.CASCADE, related_name='result')
    result_description_ru = CKEditor5Field('ru Results', config_name='extends',null=True,blank=True)
    result_description_kg = CKEditor5Field('kg Results', config_name='extends',null=True,blank=True)
    result_description_en = CKEditor5Field('en Results', config_name='extends',null=True,blank=True)


class DocumentTender(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name='documents_tender',blank=True,null=True)
    file = models.FileField(upload_to='documents_tender/',null=True,blank=True)
    description_ru = models.CharField(max_length=255,null=True,blank=True)
    description_kg = models.CharField(max_length=255,null=True,blank=True)
    description_en = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

class DocumentResultTender(models.Model):
    result = models.ForeignKey(TenderResult, on_delete=models.CASCADE, related_name='documents_result',blank=True,null=True)
    file = models.FileField(upload_to='documents_result/',null=True,blank=True)
    description_ru = models.CharField(max_length=255,null=True,blank=True)
    description_kg = models.CharField(max_length=255,null=True,blank=True)
    description_en = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)