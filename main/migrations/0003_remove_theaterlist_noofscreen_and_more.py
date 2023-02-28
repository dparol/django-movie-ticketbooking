# Generated by Django 4.1.7 on 2023-02-24 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_theaterlist_movielist_theaterlist_movielist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theaterlist',
            name='NoOfScreen',
        ),
        migrations.RemoveField(
            model_name='theaterlist',
            name='movielist',
        ),
        migrations.AddField(
            model_name='theaterlist',
            name='Screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.screen'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='Screen',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]