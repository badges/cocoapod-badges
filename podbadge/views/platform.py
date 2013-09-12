__author__ = 'Flavio'

from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.http import HttpResponse

from podbadge.utils import helpers

class PlatformView( View ):
    template_name = 'badge_platform.html'

    def get(self, request, podname, ext, retina=None):
        retina = retina or ''

        try:
            pod_info = helpers.get_pod_info(podname)

            platforms = pod_info.get('platforms', {'osx': '', 'ios': ''}).keys()
            width = 53 if len(platforms) == 1 else 74

            platforms = '/'.join(platforms)
        except Exception:
            platforms = 'error'
            width = 64

        total_width = 26 + width
        total_height = 21

        response_dict = {
            'PLATFORM': platforms,
            'WIDTH': width,
            'TOTAL_WIDTH': total_width,
            'RETINA_WIDTH': total_width * (2 if retina == '@2x' else 1),
            'RETINA_HEIGHT': total_height * (2 if retina == '@2x' else 1),
        }

        try:
            if ext == 'png':
                image_name = platforms.replace('/', '')+retina
                return HttpResponse(helpers.svg2png(image_name, response_dict, self.template_name), mimetype='image/png')
        except Exception:
            pass

        # Return svg
        return render_to_response(self.template_name, response_dict, mimetype="image/svg+xml")

############
### URLS ###
############

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^/(?P<podname>.*?)/badge(?:(?P<retina>@2x))?.(?P<ext>(png|svg))$', PlatformView.as_view()),
)