# Generated by Django 3.2 on 2021-04-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0011_project_drive_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='youtube_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]