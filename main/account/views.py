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
    - pic
    """

    # local variables with the post data:
    email = request.POST['email']
    password = request.POST['psw']
    password_repeat = request.POST['psw-repeat']
    username = request.POST['Uname']
    profile_pic = request.FILES.get('pic', None)


    #dictionary for errors:
    signup_errors = User.validate_signup(email, password, password_repeat, username, profile_pic)

    # if there are any errors, display them to the user:
    if signup_errors:
        # NOTE: I might need to change to something like this:
        #request.session['signup_errors'] = signup_errors
        #return HttpResponseRedirect(reverse('index'))
        return render(request, 'index.html', {'signup_errors': signup_errors})

    #else, create the user and log them in

    # hash password:
    password = hashers.make_password(password)

    new_user = User.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)

    #User.login()
    #return to the index
    return HttpResponseRedirect(reverse('index'))
