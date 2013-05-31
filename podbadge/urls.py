from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='http://fjcaetano.github.io/cocoapod-badges')),
    url(r'^v/(?P<podname>.*?)/badge.png$', 'podbadge.views.badge'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)