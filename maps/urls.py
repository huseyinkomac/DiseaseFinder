from django.conf.urls import include, url

from views import HomePageView, location_dataset

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^location_data/$', location_dataset, name='location')
]
