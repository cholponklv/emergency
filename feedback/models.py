from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    info_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
