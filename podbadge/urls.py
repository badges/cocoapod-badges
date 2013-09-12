from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView

# from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(
        url='http://fjcaetano.github.io/cocoapod-badges'
    )),

    url(r'^p', include('podbadge.views.platform')),
    url(r'^v', include('podbadge.views.version')),
)
