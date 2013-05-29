from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='http://fjcaetano.github.io/cocoapod-badges')),
    url(r'^v/(?P<podname>.*?)/badge.png$', 'podbadge.views.badge'),
)
