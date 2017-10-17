# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """This is the main landing page of the website"""

    #this is how we will pass db info
    #context = dict()

    return render(request, 'index.html')
