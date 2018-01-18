from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from models import Location


class HomePageView(TemplateView):
    template_name = 'index.html'


def location_dataset(request):
    location = serialize('geojson', Location.objects.all())
    return HttpResponse(location, content_type='json')
