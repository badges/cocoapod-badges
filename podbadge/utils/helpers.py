__author__ = 'Flavio'

from django.conf import settings
from django.utils import simplejson

import urllib
import urllib2
import mimetypes


def prepare_shield(vendor, status):
    url = shield_url(vendor, clean_info(status))
    return fetch_shield(url)


def shield_url(vendor, status):

    return 'http://%(service)s/%(vendor)s-%(status)s-%(color)s.png' % {
        'service': settings.SHIELD_SERVICE,
        'color': settings.SHIELD_COLOR,
        'vendor': vendor,
        'status': status,
        }


def fetch_shield(url):
    contents = urllib2.urlopen(url).read()
    mimetype = mimetypes.guess_type(url)

    return contents, mimetype


def clean_info(info):
    clean = info.replace('-', '--').replace(' ', '_')
    return urllib.quote(clean)


def get_pod_info(podname):
    url = 'http://search.cocoapods.org/api/v1/pod/%s.json' % (podname, )

    response = urllib2.urlopen(url)
    return simplejson.loads(response.read())