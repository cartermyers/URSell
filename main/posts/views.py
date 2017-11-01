# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories

def categories(request):
    return render(request, 'categories.html')
