# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-18 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_auto_20160818_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='owner',
        ),
    ]
