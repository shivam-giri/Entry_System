# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_auto_20181106_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='roomNo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
