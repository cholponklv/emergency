from django.db import models

class Point(models.Model):
    STATUS_CHOICES = [
        ('is_finished', 'is_finished'),
        ('in_progress', 'in_progress'),
        ('is_assigned', 'is_assigned'),
    ]
    name_ru = models.CharField(max_length=256,null=True,blank=True)
    name_kg = models.CharField(max_length=256,null=True,blank=True)
    name_en = models.CharField(max_length=256,null=True,blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=155)
    location = models.CharField(max_length=100,null=True,blank=True)  
    speed = models.IntegerField(null=True,blank=True)
    temperature = models.IntegerField(null=True,blank=True)
    finished = models.IntegerField(null=True,blank=True)
    depth = models.IntegerField(null=True,blank=True)
    def __str__(self):
            return self.name_ru
