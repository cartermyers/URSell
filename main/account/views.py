# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#models:
from . import models

def signup(request):
    """
    DEF: This function takes info from a POST form and creates a user

    PRE: This function assumes that the email, psw, psw-repeat, and Uname are non-null

    POST FIELDS:
    - email
    - psw
    - psw-repeat
    - Uname
    - Sid (maybe remove later)
    - pic
    - remember_user
    """

    # For now, we'll use simple validation
    # but I want to look at Django's validation more closely
    if len(request.POST['email']) < 10:
        return HttpResponse("Email is too short")

    #new_user = models.User.objects.create_user()

    #return to home page with the user now logged in
    return HttpResponseRedirect(reverse('index'))
