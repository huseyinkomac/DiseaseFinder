from django.conf.urls import include, url

from views import HomePageView, location_dataset, TheRealHomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^location_data/$', location_dataset, name='location'),
    url(r'^home/$', TheRealHomePageView.as_view(), name='index')
]
