# Generated by Django 3.2 on 2021-04-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0023_auto_20210426_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='mem1_linkedin',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem1_name',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem2_linkedin',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem2_name',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem3_linkedin',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='mem3_name',
            field=models.CharField(default='0', max_length=100),
        ),
    ]