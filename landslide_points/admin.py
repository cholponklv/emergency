from django.contrib import admin
from .models import Point
# Register your models here.
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    
    list_display = ('name_ru','name_kg','name_en', 'status', 'location','speed','temperature','finished','depth')
    list_filter = ('status', 'location')
    search_fields = ('name_ru','name_kg','name_en')
    fieldsets = (
        (None, {
            'fields': ('name_ru','name_kg','name_en', 'status', 'location','speed','temperature','finished','depth')
        }),
        ('GPS координаты', {
            'fields': ('longitude', 'latitude'),
            'classes': ('collapse',),
        }),
    )