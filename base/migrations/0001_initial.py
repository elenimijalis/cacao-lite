# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-25 22:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('flagged', models.TextField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entry_type', models.IntegerField(choices=[(0, 'Private'), (1, 'Public'), (2, 'Challenge')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GAF',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('review_state', models.IntegerField(choices=[(0, 'External'), (1, 'Unreviewed'), (2, 'Accepted'), (3, 'Rejected')], default=0)),
                ('db', models.CharField(max_length=64)),
                ('db_object_id', models.CharField(max_length=64)),
                ('db_object_symbol', models.CharField(max_length=64)),
                ('qualifier', models.CharField(blank=True, max_length=64)),
                ('go_id', models.CharField(max_length=64)),
                ('db_reference', models.CharField(max_length=64)),
                ('evidence_code', models.CharField(max_length=64)),
                ('with_or_from', models.CharField(blank=True, default='', max_length=64)),
                ('aspect', models.CharField(max_length=64)),
                ('db_object_name', models.CharField(blank=True, default='', max_length=64)),
                ('db_object_synonym', models.CharField(blank=True, default='', max_length=64)),
                ('db_object_type', models.CharField(max_length=64)),
                ('taxon', models.CharField(max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assigned_by', models.CharField(max_length=64)),
                ('annotation_extension', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('gene_product_id', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('notes', models.TextField(default='')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('superseded', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.GAF')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(null=True)),
                ('author', models.TextField(null=True)),
                ('pub_year', models.IntegerField(null=True)),
                ('title', models.TextField(null=True)),
                ('journal', models.CharField(max_length=64, null=True)),
                ('volume', models.IntegerField(null=True)),
                ('pages', models.CharField(max_length=64, null=True)),
                ('abstract', models.TextField(null=True)),
                ('keywords', models.TextField(null=True)),
                ('pmc', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_gaf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_gaf', to='base.GAF'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='original_gaf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_gaf', to='base.GAF'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='challenge',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Challenge'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='gaf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.GAF'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='gaf',
            unique_together=set([('db', 'db_object_id', 'go_id', 'db_reference', 'evidence_code', 'taxon')]),
        ),
    ]
