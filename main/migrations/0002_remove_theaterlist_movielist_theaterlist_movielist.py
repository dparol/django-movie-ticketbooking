# Generated by Django 4.1.7 on 2023-02-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theaterlist',
            name='movielist',
        ),
        migrations.AddField(
            model_name='theaterlist',
            name='movielist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
