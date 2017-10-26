# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse #temporary use

def signup(request):
    return HttpResponse("This works.")
