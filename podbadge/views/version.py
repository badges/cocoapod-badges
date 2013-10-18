__author__ = 'Flavio'

from django.views.generic.base import View
from django.http import HttpResponse

from podbadge.utils import helpers

import urllib2
import mimetypes

class VersionView( View ):
    template_name = 'badge_version.html'

    def get(self, request, podname, version=None, retina=None):
        if not version:
            try:
                pod_info = helpers.get_pod_info(podname)

                version = pod_info['version']
            except Exception:
                version = 'error'

        contents, mimetype = helpers.prepare_shield('pod', version)
        return HttpResponse(contents, mimetype=mimetype)

############
### URLS ###
############

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^/(?P<podname>.*?)/(?P<version>.*?)/badge(?:(?P<retina>@2x))?.(?:(png|svg))$', VersionView.as_view()),
    url(r'^/(?P<podname>.*?)/badge(?:(?P<retina>@2x))?.(?:(png|svg))$', VersionView.as_view()),
)