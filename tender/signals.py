from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Tender,TenderResult
import re

@receiver(pre_save, sender=Tender)
def update_description(sender, instance, **kwargs):
    description_content = instance.description
    description_content = re.sub(r'src="(/media/[^"]+)"', r'src="http://195.38.165.74:8000\1"', description_content)
    instance.description = description_content

@receiver(pre_save, sender=TenderResult)
def update_description(sender, instance, **kwargs):
    result_content = instance.result_description
    result_content = re.sub(r'src="(/media/[^"]+)"', r'src="http://195.38.165.74:8000\1"', result_content)
    instance.result_description = result_content
