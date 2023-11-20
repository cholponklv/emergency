from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Feedback(models.Model):
    phone_number = PhoneNumberField(unique = True)
    info_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

