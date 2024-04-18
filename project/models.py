from django.db import models

class Project(models.Model):
    name_ru = models.CharField(max_length=256,null=True,blank=True)
    name_kg = models.CharField(max_length=256,null=True,blank=True)
    name_en = models.CharField(max_length=256,null=True,blank=True)
    description_ru = models.TextField(null=True,blank=True)
    description_kg = models.TextField(null=True,blank=True)
    description_en = models.TextField(null=True,blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos',null=True,blank=True)
    image = models.ImageField(upload_to='photos/',null=True,blank=True)
    caption_ru = models.CharField(max_length=255, blank=True, null=True)
    caption_kg = models.CharField(max_length=255, blank=True, null=True)
    caption_en = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents',blank=True,null=True)
    file = models.FileField(upload_to='documents/',null=True,blank=True)
    description_ru = models.CharField(max_length=255,null=True,blank=True)
    description_kg = models.CharField(max_length=255,null=True,blank=True)
    description_en = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

