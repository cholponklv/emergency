# Generated by Django 4.2.6 on 2024-04-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_points', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]