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
    list_display = ('name', 'description','created_at')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('project', 'image', 'caption','created_at')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('project', 'file', 'description','created_at')
