__author__ = 'flaviocaetano'

from django.shortcuts import render_to_response
from django.utils import simplejson
from django.conf import settings
from lxml import etree

import os, urllib2, StringIO

def badge(request, podname):
    podname = podname.lower()

    url = 'http://cocoapods.org/search?query=name:%s&ids=999&offset=0' % podname

    try:
        response = urllib2.urlopen(url)
        pod_info = simplejson.loads(response.read())

        allocations = pod_info['allocations'][0]

        index = 0
        for result in allocations[4]:
            name = result.lower()
            if name == podname:
                break

            index += 1

        xml = StringIO.StringIO(allocations[5][index])

        tree = etree.parse(xml)
        for e in tree.xpath('//span[@class="version"]'):
            version = e.text.strip()
            break

        version = version if name.lower() == podname else 'error'
    except Exception, e:
        version = 'error'

    return render_to_response('badge_version.html', {'VERSION':version}, mimetype="image/svg+xml")