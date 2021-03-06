# Generated by Django 3.2 on 2021-04-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0017_alter_feedback_project_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='project_dept',
            field=models.CharField(choices=[('it', 'IT'), ('comps', 'COMPS'), ('extc', 'EXTC'), ('mech', 'MECH')], default='IT', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='dept',
            field=models.CharField(choices=[('it', 'IT'), ('comps', 'COMPS'), ('extc', 'EXTC'), ('mech', 'MECH')], default='it', max_length=6),
        ),
    ]
