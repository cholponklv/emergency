from django.contrib import admin
from .models import News
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_ru','title_kg','title_en', 'created_at','target_ru','target_kg','target_en','photo')
    list_filter = ('created_at',)
    search_fields = ('title_ru','target_kg','target_en','created_at')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Опубликовать выбранные новости"
    
