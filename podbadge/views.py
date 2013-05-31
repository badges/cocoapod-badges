__author__ = 'flaviocaetano'

from django.http import HttpResponse
from django.utils import simplejson
from django.conf import settings
from lxml import etree

import os, urllib2, pprint, StringIO

def badge(request, podname):
    podname = podname.lower()
    svg_path = os.path.join(settings.PROJECT_ROOT, 'badge_version.svg')

    url = 'http://cocoapods.org/search?query=name:%s&ids=999&offset=0' % podname

    with open(svg_path, 'r') as svg_file:
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

        svg_data = svg_file.read() % (version, version)
        return HttpResponse(svg_data, mimetype="image/svg+xml")