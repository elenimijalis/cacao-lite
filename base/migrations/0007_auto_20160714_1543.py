# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-14 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20160712_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaf',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
