# Generated by Django 4.1.2 on 2022-10-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_task_time_alter_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
