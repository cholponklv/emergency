# Generated by Django 4.2.6 on 2024-03-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'Январь'), ('February', 'Февраль'), ('March', 'Март'), ('April', 'Апрель'), ('May', 'Май'), ('June', 'Июнь'), ('July', 'Июль'), ('August', 'Август'), ('September', 'Сентябрь'), ('October', 'Октябрь'), ('November', 'Ноябрь'), ('December', 'Декабрь')], max_length=120)),
                ('value', models.IntegerField()),
                ('type', models.CharField(choices=[('Plan', 'План'), ('Actual', 'Факт')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Graph2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Acceptable', 'Приемлемый'), ('Concerning', 'Тревожный'), ('Critical', 'Критический')], max_length=200)),
                ('month', models.CharField(choices=[('January', 'Январь'), ('February', 'Февраль'), ('March', 'Март'), ('April', 'Апрель'), ('May', 'Май'), ('June', 'Июнь'), ('July', 'Июль'), ('August', 'Август'), ('September', 'Сентябрь'), ('October', 'Октябрь'), ('November', 'Ноябрь'), ('December', 'Декабрь')], max_length=200)),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Graph3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'Январь'), ('February', 'Февраль'), ('March', 'Март'), ('April', 'Апрель'), ('May', 'Май'), ('June', 'Июнь'), ('July', 'Июль'), ('August', 'Август'), ('September', 'Сентябрь'), ('October', 'Октябрь'), ('November', 'Ноябрь'), ('December', 'Декабрь')], max_length=200)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Graph4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('costs', models.IntegerField()),
            ],
        ),
    ]