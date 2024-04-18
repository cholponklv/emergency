# Generated by Django 4.2.6 on 2024-04-17 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0006_remove_tender_description_remove_tender_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tender',
            old_name='en_description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='kg_description',
            new_name='description_kg',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='ru_description',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='en_name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='kg_name',
            new_name='name_kg',
        ),
        migrations.RenameField(
            model_name='tender',
            old_name='ru_name',
            new_name='name_ru',
        ),
        migrations.RenameField(
            model_name='tenderresult',
            old_name='en_result_description',
            new_name='result_description_en',
        ),
        migrations.RenameField(
            model_name='tenderresult',
            old_name='kg_result_description',
            new_name='result_description_kg',
        ),
        migrations.RenameField(
            model_name='tenderresult',
            old_name='ru_result_description',
            new_name='result_description_ru',
        ),
    ]
