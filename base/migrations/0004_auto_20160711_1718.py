# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-11 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160708_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='journal',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='keywords',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pmid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pub_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='volume',
            field=models.IntegerField(null=True),
        ),
    ]
