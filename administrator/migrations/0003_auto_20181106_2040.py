# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_auto_20181106_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fName',
            new_name='fatherName',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mName',
            new_name='motherName',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='pEmail',
            new_name='parentEmail',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='pNumber',
            new_name='parentNumber',
        ),
    ]
