__author__ = 'flaviocaetano'

from django.shortcuts import render_to_response
from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse

import urllib2
import os


def version(request, podname):
    try:
        pod_info = get_pod_info(podname)

        version = pod_info['version']
    except urllib2.HTTPError:
        version = 'error'

    except Exception:
        version = 'error'

    width = 44+5*len(version)
    total_width = 25 + width

    return render_to_response('badge_version.html', {
        'VERSION': version,
        'WIDTH': width,
        'TOTAL_WIDTH': total_width,
    }, mimetype="image/svg+xml")


def platform(request, podname, ext):
    try:
        pod_info = get_pod_info(podname)

        platforms = pod_info.get('platforms', {'osx': '', 'ios': ''}).keys()
        width = 62 if len(platforms) == 1 else 86

        platforms = '/'.join(platforms)
    except Exception:
        platforms = 'error'
        width = 75

    total_width = 25 + width

    try:
        if ext == 'png':

            image_path = os.path.join(
                settings.STATIC_ROOT,
                platforms.replace('/', '')+'.png'
            )
            # Return image
            with open(image_path, 'r') as file:
                return HttpResponse(file.read(), mimetype='image/png')
    except Exception:
        pass

    # Return svg
    return render_to_response('badge_platform.html', {
        'PLATFORM': platforms,
        'WIDTH': width,
        'TOTAL_WIDTH': total_width,
    }, mimetype="image/svg+xml")


def badge(request, info, podname, ext):
    if info == 'p':
        return platform(request, podname, ext)

    return version(request, podname)


def get_pod_info(podname):
    url = 'http://cocoapods.org/api/v1/pod/%s.json' % (podname, )

    response = urllib2.urlopen(url)
    return simplejson.loads(response.read())
