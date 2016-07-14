# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-14 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20160714_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='gaf',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='annotation',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='annotation',
        ),
        migrations.AddField(
            model_name='assessment',
            name='gaf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.GAF'),
        ),
        migrations.AddField(
            model_name='gaf',
            name='uuid',
            field=uuidfield.fields.UUIDField(blank=True, editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='gaf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.GAF'),
        ),
        migrations.DeleteModel(
            name='Annotation',
        ),
    ]
