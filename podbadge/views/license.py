__author__ = 'Flavio'

from django.views.generic.base import View
from django.views.decorators.cache import never_cache
from django.http import HttpResponsePermanentRedirect

from django.conf import settings

class LicenseView( View ):
    template_name = 'badge_version.html'

    @never_cache
    def get(self, request, podname):
        return HttpResponsePermanentRedirect(settings.SHIELD_SERVICE % {'status': 'l', 'vendor': podname} )

############
### URLS ###
############

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^/(?P<podname>.*?)', LicenseView.as_view()),
)