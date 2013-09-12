__author__ = 'Flavio'

from django.conf import settings
from django.shortcuts import render_to_response

import os
import cairosvg

def svg2png(image_name, response_dict, template_name):

    image_path = os.path.join(
        settings.STATIC_ROOT,
        image_name+'.png'
    )

    # Convert to PNG if the image doesn't exists
    if not os.path.exists(image_path):
        response = render_to_response(template_name, response_dict)

        with open(image_path, 'w') as file:
            cairosvg.svg2png(bytestring=response.content, write_to=file)

    # Return image
    with open(image_path, 'r') as file:
        return file.read()