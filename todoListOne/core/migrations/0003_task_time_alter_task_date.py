# Generated by Django 4.1.2 on 2022-10-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]