__author__ = 'Flavio'

from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.http import HttpResponse

from podbadge.utils import helpers

class VersionView( View ):
    template_name = 'badge_version.html'

    def get(self, request, podname, ext, retina=None, version=None):
        retina = retina or ''

        if not version:
            try:
                pod_info = helpers.get_pod_info(podname)

                version = pod_info['version']
            except Exception:
                version = 'error'

        width = 33+5*len(version)
        total_width = 26 + width
        total_height = 21

        response_dict = {
            'VERSION': version,
            'WIDTH': width,
            'TOTAL_WIDTH': total_width,
            'RETINA_WIDTH': total_width * (2 if retina == '@2x' else 1),
            'RETINA_HEIGHT': total_height * (2 if retina == '@2x' else 1),
        }

        try:
            if ext == 'png':
                image_name = version+retina
                return HttpResponse(helpers.svg2png(image_name, response_dict, self.template_name), mimetype='image/png')
        except Exception:
            raise
            pass

        return render_to_response(self.template_name, response_dict, mimetype="image/svg+xml")

############
### URLS ###
############

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^/(?P<podname>.*?)/(?P<version>.*?)/badge(?:(?P<retina>@2x))?.(?P<ext>(png|svg))$', VersionView.as_view()),
    url(r'^/(?P<podname>.*?)/badge(?:(?P<retina>@2x))?.(?P<ext>(png|svg))$', VersionView.as_view()),
)