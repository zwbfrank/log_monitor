# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_analyze', '0002_auto_20171014_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdata',
            name='content',
            field=models.TextField(),
        ),
    ]