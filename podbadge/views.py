__author__ = 'flaviocaetano'

from django.http import HttpResponse
from django.utils import simplejson
from django.conf import settings

import os, datetime, urllib2

def badge(request, podname):
    json_path = os.path.join(settings.PROJECT_ROOT, 'documents.jsonp')
    svg_path = os.path.join(settings.PROJECT_ROOT, 'badge_version.svg')

    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(json_path))
    datediff = datetime.datetime.now() - file_time
    print datediff

    if datediff.seconds > 60*60: # uma hora
        download_documents(json_path)

    with open(json_path, 'r') as file, open(svg_path, 'r') as svg_file:
        json_file = file.read()

        pod_list= simplejson.loads(json_file)

        version = 'error'

        for item in pod_list:
            if item['name'].lower() == podname:
                version = item['versions'][-1]

        svg_data = svg_file.read().format(version)
        return HttpResponse(svg_data, mimetype="image/svg+xml")

def download_documents(file_path):
    with open(file_path, "w") as file:
        response = urllib2.urlopen('http://cocoadocs.org/documents.jsonp')

        file.write(response.read()[12:-21])