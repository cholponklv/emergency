from django.db import models

# Create your models here.
from django.db import models

class Graph1(models.Model):
    MONTH_CHOICES = [
        ('January', 'Январь'),
        ('February', 'Февраль'),
        ('March', 'Март'),
        ('April', 'Апрель'),
        ('May', 'Май'),
        ('June', 'Июнь'),
        ('July', 'Июль'),
        ('August', 'Август'),
        ('September', 'Сентябрь'),
        ('October', 'Октябрь'),
        ('November', 'Ноябрь'),
        ('December', 'Декабрь'),
    ]
    
    TYPE_CHOICES = [
        ('Plan', 'План'),
        ('Actual', 'Факт'),
    ]
    
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    value = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)


class Graph2(models.Model):
    TYPE_CHOICES = [
        ('Acceptable', 'Приемлемый'),
        ('Concerning', 'Тревожный'),
        ('Critical', 'Критический'),
    ]
    
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    x = models.IntegerField()
    y = models.IntegerField()


class Graph3(models.Model):
    MONTH_CHOICES = [
        ('January', 'Январь'),
        ('February', 'Февраль'),
        ('March', 'Март'),
        ('April', 'Апрель'),
        ('May', 'Май'),
        ('June', 'Июнь'),
        ('July', 'Июль'),
        ('August', 'Август'),
        ('September', 'Сентябрь'),
        ('October', 'Октябрь'),
        ('November', 'Ноябрь'),
        ('December', 'Декабрь'),
    ]
    
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    value = models.IntegerField()

class Graph4(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    costs = models.IntegerField()
