# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_analyze', '0004_auto_20171017_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdata',
            name='log_level',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='logdata',
            name='log_type',
            field=models.CharField(max_length=225),
        ),
    ]
