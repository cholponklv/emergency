from django.db import models
from project.models import Project
# Create your models here.
from django_ckeditor_5.fields import CKEditor5Field

class News(models.Model):
    title = models.CharField(max_length=160)
    target = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    





    