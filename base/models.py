from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from uuidfield import UUIDField


ENTRY_TYPES = (
    (0, 'Private'),
    (1, 'Public'),
    (2, 'Challenge'),
)

FLAGGED = (
    (0, 'Protein'),
    (1, 'Publication'),
    (2, 'Qualifier'),
    (3, 'Go term'),
    (4, 'Evidence'),
    (5, 'Originality'),
)

class Team(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

class GAF(models.Model):
    db = models.CharField(max_length=64)
    db_object_id = models.CharField(max_length=64)
    db_object_symbol = models.CharField(max_length=64)
    Qualifier = models.CharField(max_length=64)
    go_id = models.CharField(max_length=64)
    db_reference = models.CharField(max_length=64)
    evidence_code = models.CharField(max_length=64)
    with_or_from = models.CharField(max_length=64)
    aspect = models.CharField(max_length=64)
    db_object_name = models.CharField(max_length=64)
    db_object_synonym = models.CharField(max_length=64)
    db_object_type = models.CharField(max_length=64)
    taxon = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    assigned_by = models.CharField(max_length=64)
    annotation_extension = models.CharField(max_length=64)
    gene_product_id = models.CharField(max_length=64)

class Annotation(models.Model):
    uuid = UUIDField(auto=True)
    gaf = models.ForeignKey(GAF)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

class Challenge(models.Model):
    uuid = UUIDField(auto=True)
    user = models.ForeignKey(User)
    annotation = models.ForeignKey(Annotation)
    entry_type = models.IntegerField(choices=ENTRY_TYPES, default=0)
    date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

class Assessment(models.Model):
    annotation = models.ForeignKey(Annotation)
    challenge = models.ForeignKey(Challenge)
    flagged = MultiSelectField(choices=FLAGGED, max_choices=6, default=0, blank=True)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)