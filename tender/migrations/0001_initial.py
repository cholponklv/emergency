# Generated by Django 4.2.6 on 2024-04-18 09:30

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('name_kg', models.CharField(blank=True, max_length=256, null=True)),
                ('name_en', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateField()),
                ('deadline', models.DateField()),
                ('description_ru', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='ru Description')),
                ('description_kg', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='kg Description')),
                ('description_en', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='en Description')),
                ('status', models.CharField(choices=[('progress', 'В процессе'), ('finished', 'Закончен')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TenderResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_description_ru', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='ru Results')),
                ('result_description_kg', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='kg Results')),
                ('result_description_en', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='en Results')),
                ('tender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='tender.tender')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentTender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents_tender/')),
                ('description_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('description_kg', models.CharField(blank=True, max_length=255, null=True)),
                ('description_en', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('tender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_tender', to='tender.tender')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentResultTender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents_result/')),
                ('description_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('description_kg', models.CharField(blank=True, max_length=255, null=True)),
                ('description_en', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_result', to='tender.tenderresult')),
            ],
        ),
    ]
