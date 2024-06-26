import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.conf import settings

class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""
    
    location = os.path.join(settings.MEDIA_ROOT, "photo_edit")
    base_url = settings.MY_SITE_BASE_URL + settings.MEDIA_URL + "photo_edit/"