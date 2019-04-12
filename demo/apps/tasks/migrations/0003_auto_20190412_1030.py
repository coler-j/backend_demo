# Generated by Django 2.2 on 2019-04-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190412_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
