# Generated by Django 5.1.5 on 2025-01-23 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtask',
            old_name='addtask',
            new_name='task_name',
        ),
    ]
