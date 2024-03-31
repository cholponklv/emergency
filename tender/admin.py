from django.contrib import admin
from .models import Tender,TenderResult
# Register your models here.

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'created_at','description')
    list_filter = ('name', 'deadline')
    search_fields = ('name',)
admin.site.register(TenderResult)