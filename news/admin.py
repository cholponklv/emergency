from django.contrib import admin
from .models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','description','photo', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Опубликовать выбранные новости"
    