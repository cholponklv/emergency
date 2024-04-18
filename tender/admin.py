from django.contrib import admin
from .models import Tender,TenderResult,DocumentTender,DocumentResultTender
# Register your models here.
class DocumentInline(admin.TabularInline):
    model = DocumentTender
    extra = 1

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]
    list_display = ('name_ru','name_kg','name_en', 'deadline', 'created_at','description_ru','description_kg','description_en')
    list_filter = ('name_ru','name_kg','name_en', 'deadline')
    search_fields = ('name_ru','name_kg','name_en',)

class DocumentResultInline(admin.TabularInline):
    model = DocumentResultTender
    extra = 1
@admin.register(TenderResult)
class TenderResultAdmin(admin.ModelAdmin):
    inlines = [DocumentResultInline]
    list_display = ('tender','result_description_ru','result_description_kg','result_description_en')
admin.site.register(DocumentTender)
admin.site.register(DocumentResultTender)
