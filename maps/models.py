from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class Location(models.Model):
    text = models.CharField(max_length=142)
    created_at = models.DateField()
    types = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.text
