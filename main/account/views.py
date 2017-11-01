# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password

import re

#models:
from .models import User

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
    """

    # local variables with the post data:
    email = request.POST['email']
    password = request.POST['psw']
    password_repeat = request.POST['psw-repeat']
    username = request.POST['Uname']
    sid = request.POST['Sid']
    profile_pic = request.POST['pic']
    remember_user = request.POST['remember_user']

    #dictionary for errors:
    signup_errors = User.signup(email, password, password_repeat, username, profile_pic) 

       # TODO: check sid?
    #       check profile pic?
    #       save profile pic (handle in models)
    #       use cookies for remember_user
    #       log in user if successful
    #       send user error if unsuccessful

    # if there are any errors, display them to the user:
    if signup_errors:
        return render(request, 'index.html', {'signup_errors': signup_errors})

    #else, create the user and log them in
    new_user = User.objects.create_user(username=username, email=email, password=password)

    #User.login()
    #return to the index
    return HttpResponseRedirect(reverse('index'))
