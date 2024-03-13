from django.contrib import admin
from .models import Point
# Register your models here.
@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'location','speed','temperature','finished','depth')
    list_filter = ('status', 'location')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'status', 'location')
        }),
        ('GPS координаты', {
            'fields': ('longitude', 'latitude'),
            'classes': ('collapse',),
        }),
    )