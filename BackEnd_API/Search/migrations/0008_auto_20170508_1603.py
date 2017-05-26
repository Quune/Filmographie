# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0007_remove_season_plot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='episodes',
        ),
        migrations.RemoveField(
            model_name='movieseriedetails',
            name='season',
        ),
        migrations.AddField(
            model_name='movieseriedetails',
            name='episodes',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Search.Episode'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]