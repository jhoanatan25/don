# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20170116_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='iframe',
        ),
    ]
