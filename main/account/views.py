# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import hashers
# from django.backends.base import SessionBase

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
    new_user = User.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)

    # log in user:
    request.session['logged_in'] = new_user.pk
    #return to the index
    return HttpResponseRedirect(reverse('index'))

def login(request):
    """
    DEF: This function is the from handler for logging in users.

    PRE: POST['uname'] and POST['psw'] are non-null.

    POST: A user is logged in or an error is thrown. Either way, they are
    redirected back to the homepage
    """

	#if user is already signed in, redirect them
    if request.session.get('logged_in', None):
		return render(request, 'index.html')

    username = request.POST['uname']
    password = request.POST['psw']
    keep_log_in = request.POST.get('keep_log_in', None)

    user = User()
    login_errors = user.login(username, password)

    if login_errors:
		return render(request, 'index.html', {'login_errors': login_errors})

    request.session['logged_in'] = user.pk

    if keep_log_in:
		request.session.set_expiry(60 * 60 * 24 * 10) # set expiry for 10 days
    else:
        pass
        #request.session.set_expiry(0)	# expires on browser close

    return HttpResponseRedirect(reverse('index'))

def logout(request):
    try:
        del request.session['logged_in']
        request.session.flush()
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('index'))
