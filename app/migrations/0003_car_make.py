# Generated by Django 5.1.6 on 2025-02-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='make',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
