# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='rate',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='episode',
            name='runtime',
            field=models.TimeField(),
        ),
    ]
