from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import News
import re

@receiver(pre_save, sender=News)
def update_target(sender, instance, **kwargs):
    target_content = instance.target
    target_content = re.sub(r'src="(/media/[^"]+)"', r'src="http://195.38.165.74:8000\1"', target_content)
    instance.target = target_content
