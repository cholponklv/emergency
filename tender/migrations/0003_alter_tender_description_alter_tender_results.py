# Generated by Django 4.2.6 on 2024-03-27 09:24

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0002_tender_results_tender_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='results',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Results'),
        ),
    ]
