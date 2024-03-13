# Generated by Django 4.2.6 on 2024-03-13 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='goals',
            name='project',
        ),
        migrations.RemoveField(
            model_name='memberteam',
            name='team',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='project',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='project',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='project.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.DeleteModel(
            name='MemberTeam',
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='project.project'),
        ),
    ]
