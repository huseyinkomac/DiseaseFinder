from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class Location(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    coordinates = models.PointField(srid=4326)
    objects = models.GeoManager()
    type = models.CharField(max_length=255)
