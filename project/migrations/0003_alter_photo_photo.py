# Generated by Django 4.2.6 on 2023-11-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_photo_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photo'),
        ),
    ]
