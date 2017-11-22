# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """This is the main landing page of the website"""

    #this is how we will pass db info
    #context = dict()

    return render(request, 'index.html')

# here is a generic function for image file checking:
def image_validation(file_list):
    for f in file_list:
        ext = f.name.split('.')[-1]
        if ext.lower() not in ['jpg', 'png', 'jpeg', 'tiff', 'gif']:
            return False
    return True
