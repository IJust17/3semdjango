# Generated by Django 4.2.9 on 2025-01-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='sort_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalfile',
            name='sort_index',
            field=models.IntegerField(default=0),
        ),
    ]
