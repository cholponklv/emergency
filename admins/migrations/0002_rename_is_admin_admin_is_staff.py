# Generated by Django 4.2.6 on 2023-11-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
