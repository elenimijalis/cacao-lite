# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20160901_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organism',
            name='alternate_name',
        ),
        migrations.AddField(
            model_name='gene',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
