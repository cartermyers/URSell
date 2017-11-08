# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import hashers, authenticate, login, logout

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

    # create_user hashes the password for us
    if profile_pic:
        new_user = User.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)
    else:
        new_user = User.objects.create_user(username=username, email=email, password=password)


    # log in user:
    login(request, new_user)

    #return to the index
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    """
    DEF: This function is the from handler for logging in users.

    PRE: POST['uname'] and POST['psw'] are non-null.

    POST: A user is logged in or an error is thrown. Either way, they are
    redirected back to the homepage
    """

	#if user is already signed in, redirect them
    #NOTE: I'm not sure if this is actually necessary
    #if request.user.is_authenticated:
        #HttpResponseRedirect(reverse('index'))

    username = request.POST['uname']
    password = request.POST['psw']
    keep_log_in = request.POST.get('keep_log_in', None)

    user = authenticate(request, username=username, password=password)

    # if user is not None, then there are no errors
    if user:
        login(request, user)
    else:
        return render(request, 'index.html', {'login_errors': 'Those are invalid credentials'})

    if keep_log_in:
		request.session.set_expiry(60 * 60 * 24 * 10) # set expiry for 10 days

    #else, uses the default expiry at browser close

    return HttpResponseRedirect(reverse('index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
