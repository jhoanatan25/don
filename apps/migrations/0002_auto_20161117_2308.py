# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
