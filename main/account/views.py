# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import hashers, authenticate, login, logout, decorators

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
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['psw']
        password_repeat = request.POST['psw-repeat']
        username = request.POST['Uname']
        profile_pic = request.FILES.get('pic', None)


        #dictionary for errors:
        signup_errors = User.validate_signup(email, password, password_repeat, username)

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

    # this holds where the users should be redirected to
    redirect = request.GET.get('next', reverse('index'))

    if request.method == "POST":

        username = request.POST['uname']
        password = request.POST['psw']
        keep_log_in = request.POST.get('keep_log_in', None)

        user = authenticate(request, username=username, password=password)

        # if user is not None, then there are no errors
        if user:
            login(request, user)
        else:
            return render(request, 'account/login.html', {'login_errors': 'Those are invalid credentials'})

        if keep_log_in:
		          request.session.set_expiry(60 * 60 * 24 * 10) # set expiry for 10 days

        #else, uses the default expiry at browser close

    return HttpResponseRedirect(redirect)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def validate_email(request, user_id):
    """NOTE: this is just a temporary implementation for testing"""

    if not user_id:
        request.user.send_validation_email()
    else:
        user = get_object_or_404(User, pk=user_id)
        user.validated_email = True
        user.save()
    return HttpResponseRedirect(reverse('index'))

    """
    NOTE: here is a more general view for sending/receiving requests.
        From a security view, there needs to be better checking if the
        email was actually sent, if they responded from the email, etc.

    context = dict()
    if request.method == 'POST':
        request.user.send_validation_email()
        context['message'] = "An email has been sent to " + request.user.email + " for validation"
    elif user_id:
        user = get_object_or_404(User, pk=user_id)
        user.validated_email = True
        user.save()
        context['message'] = "Your email is now validated!"


    return HttpResponseRedirect(reverse(request.GET['next']))
    """
