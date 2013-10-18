__author__ = 'Flavio'

from django.views.generic.base import View
from django.http import HttpResponse

from podbadge.utils import helpers


class PlatformView(View):
    template_name = 'badge_platform.html'

    def get(self, request, podname, retina=None):

        try:
            pod_info = helpers.get_pod_info(podname)

            platforms = pod_info.get('platforms', {'osx': '', 'ios': ''}).keys()

            platforms = '|'.join(platforms)
        except Exception:
            platforms = 'error'

        contents, mimetype = helpers.prepare_shield('platform', platforms)
        return HttpResponse(contents, mimetype=mimetype)

############
### URLS ###
############

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^/(?P<podname>.*?)/badge(?:(?P<retina>@2x))?.(?:(png|svg))$', PlatformView.as_view()),
)