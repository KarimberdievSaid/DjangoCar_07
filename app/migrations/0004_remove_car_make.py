# Generated by Django 5.1.6 on 2025-02-18 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_car_make'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='make',
        ),
    ]
