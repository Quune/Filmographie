# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0006_auto_20170507_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='plot',
        ),
    ]
