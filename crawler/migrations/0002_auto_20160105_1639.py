# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Post',
        ),
    ]
