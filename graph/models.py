from django.db import models

# Create your models here.
from django.db import models

class Graph1(models.Model):
    MONTH_CHOICES = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]
    
    TYPE_CHOICES = [
        ('Plan', 'План'),
        ('Actual', 'Факт'),
    ]
    
    month = models.CharField(max_length=120, choices=MONTH_CHOICES)
    value = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    def __str__(self):
        return self.month

class Graph2(models.Model):
    TYPE_CHOICES = [
        ('Acceptable', 'Приемлемый'),
        ('Concerning', 'Тревожный'),
        ('Critical', 'Критический'),
    ]
    MONTH_CHOICES = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    month = models.CharField(max_length=200, choices=MONTH_CHOICES)
    x = models.IntegerField(null=True,blank=True)
    y = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.month


class Graph3(models.Model):
    MONTH_CHOICES = [
        ('Январь', 'Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),
    ]
    month = models.CharField(max_length=200, choices=MONTH_CHOICES)
    value = models.IntegerField()
    def __str__(self):
        return self.month

class Graph4(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    costs = models.IntegerField()
    def __str__(self):
            return self.name