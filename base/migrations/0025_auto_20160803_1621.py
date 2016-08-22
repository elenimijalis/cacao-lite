# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-03 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20160803_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gaf',
            name='challenge_gaf',
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_gaf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_gaf', to='base.GAF'),
        ),
    ]