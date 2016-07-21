# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-21 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20160714_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaf',
            name='review_state',
            field=models.IntegerField(choices=[(0, 'External'), (1, 'Unreviewed'), (2, 'Accepted'), (3, 'Rejected')], default=0),
        ),
    ]
