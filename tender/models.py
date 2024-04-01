from django.db import models
from project.models import Project
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Tender(models.Model):
    TYPE_CHOICES = [
        ('progress', 'В процессе'),
        ('finished', 'Закончен'),
    ]
    name = models.CharField(max_length=144)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    description = CKEditor5Field('Description', config_name='extends')
    status = models.CharField(max_length=200, choices=TYPE_CHOICES)
    def __str__(self):
            return self.name

class TenderResult(models.Model):
    tender = models.OneToOneField('Tender', on_delete=models.CASCADE, related_name='result')
    result_description = CKEditor5Field('Results', config_name='extends')
    def __str__(self):
            return self.tender


