# Generated by Django 4.2.6 on 2024-04-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0005_alter_graph1_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph4',
            name='created_at',
            field=models.DateField(),
        ),
    ]