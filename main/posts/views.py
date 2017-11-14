# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories

def new_post(request):
    """ a view to handle and present the new post form
        post fields include:

        1
        - adtitle (text)
        - type (radio: offering/wanting)
        - price (investigate this input more)
        - saletype (radio: different inputs)
        - NOTE: NAME NEEDED description

        2
        - Image array (NEEDS DIFFERENT NAMES)

        3
        - user_bio (text: location)

        4
        - detail (selection, basically a category)

        5
        - tel (phone number) NOTE: is this needed?
        - email NOTE: is this needed? """

    errors = dict()

    #


    return render(request, 'posts/categories.html', {'errors': errors})

def categories(request):
    return render(request, 'posts/categories.html')

def categories_test(request):
    return render(request, 'posts/categoriestest.html')

def test(request):
    return render(request, 'posts/test.html')
