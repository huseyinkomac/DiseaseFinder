from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    coordinates = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
