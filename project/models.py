from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='team_photo')
    phone = PhoneNumberField(unique = True)



class MemberTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)





class Project(models.Model):
    STATUS_CHOICES = [
        ('is_finished', 'is_finished'),
        ('in_progress', 'in_progress'),
        ('is_assigned', 'is_assigned'),
    ]



    name = models.CharField(max_length=256)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=155)
    description = models.TextField()
    owner = models.CharField(max_length=140)
    budget = models.IntegerField()
    deadline = models.DateField()
    start_at = models.DateField(auto_now_add=True)
    color = models.CharField(max_length=100)
