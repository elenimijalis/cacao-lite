# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-14 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20160714_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaf',
            name='annotation_extension',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='gaf',
            name='gene_product_id',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
    ]
