import os
from django.contrib.gis.utils import LayerMapping
from .models import Location

location_mapping = {
    'text': 'text',
    'created_at': 'created_at',
    'types': 'types',
    'geom': 'POINT',
}

location_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'datas/OGRGeoJSON.shp'))


def run(verbose=True):
    lm = LayerMapping(Location, location_shp, location_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
