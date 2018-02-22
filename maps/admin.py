from django.contrib import admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin
# Register your models here.


class LocationAdmin(LeafletGeoAdmin):
    list_display = ('text', 'created_at', 'types')


admin.site.register(Location, LocationAdmin)
