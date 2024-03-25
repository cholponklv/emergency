from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Feedback
from django.conf import settings

@receiver(post_save, sender=Feedback)
def send_email_on_creation(sender, instance, created, **kwargs):
    if created:
        email_tht_send = instance.email
        subject = 'feedback'
        message = f'{instance.info_text} from {email_tht_send},{instance.name}. Created at {instance.created_at}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]

        send_mail(subject, message, email_from, recipient_list)