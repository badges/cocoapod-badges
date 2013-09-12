__author__ = 'flaviocaetano'

from django.shortcuts import render_to_response
from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse

from podbadge.utils import helpers

import cairosvg
import urllib2
import os


def version(request, podname, ext, retina=''):
    template_name = 'badge_version.html'

    retina = retina or ''

    try:
        pod_info = get_pod_info(podname)

        version = pod_info['version']
    except urllib2.HTTPError:
        version = 'error'

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
            return HttpResponse(helpers.svg2png(image_name, response_dict, template_name), mimetype='image/png')
    except Exception:
        raise
        pass

    return render_to_response(template_name, response_dict, mimetype="image/svg+xml")


def platform(request, podname, ext, retina=''):
    template_name = 'badge_platform.html'

    retina = retina or ''

    try:
        pod_info = get_pod_info(podname)

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
            return HttpResponse(helpers.svg2png(image_name, response_dict, 'badge_platform.html'), mimetype='image/png')
    except Exception:
        pass

    # Return svg
    return render_to_response(template_name, response_dict, mimetype="image/svg+xml")


def badge(request, info, podname, ext, retina=False):
    if info == 'p':
        return platform(request, podname, ext, retina)

    return version(request, podname, ext, retina)


def get_pod_info(podname):
    url = 'http://cocoapods.org/api/v1/pod/%s.json' % (podname, )

    response = urllib2.urlopen(url)
    return simplejson.loads(response.read())
