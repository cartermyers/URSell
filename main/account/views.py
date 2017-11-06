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
    signup_errors = dict()

    # For now, we'll use simple validation
    # but I want to look at Django's validation more closely

    # ---- email ----

    # u of r email
    if not re.match(r"\S{3,}@uregina.ca$", email):
        signup_errors['email'] = "Must be a valid University of Regina email."

    # reject the email if it already is registered
    try:
        User.objects.get(email=email)
        signup_errors['email'] = "Email is already registered"
    except User.DoesNotExist:
        pass

    # check if passwords match
    if password != password_repeat:
        signup_errors['password'] = "Your passwords did not match."

    # hash password:
    password = make_password(password)

    #unique username
    try:
        User.objects.get(username=username)
        signup_errors['username'] = "Username already exists."
    except User.DoesNotExist:
        pass

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

    #return to the index
    return HttpResponseRedirect(reverse('index'))
