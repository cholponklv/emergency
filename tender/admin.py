from django.contrib import admin
from .models import Tender
# Register your models here.

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'created_at')
    list_filter = ('name', 'deadline')
    search_fields = ('name',)