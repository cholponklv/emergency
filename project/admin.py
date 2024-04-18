from django.contrib import admin
from .models import Project, Photo, Document

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, DocumentInline]
    list_display = ('name_ru','name_kg','name_en', 'description_ru','description_kg','description_en','created_at')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('project', 'image', 'caption_ru','caption_kg','caption_en','created_at')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('project', 'file', 'description_ru','description_kg','description_en','created_at')
