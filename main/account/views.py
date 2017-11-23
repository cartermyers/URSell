# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import hashers, authenticate, login, logout, decorators
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import re

#models:
from .models import User
from .tokens import account_activation_token

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
    if request.method == "POST" and not request.user.is_authenticated:
        email = request.POST['email']
        password = request.POST['psw']
        password_repeat = request.POST['psw-repeat']
        username = request.POST['Uname']
        profile_pic = request.FILES.get('pic', None)

        #dictionary for errors:
        signup_errors = User.validate_signup(email, password, password_repeat, username, profile_pic)

        # if there are any errors, display them to the user:
        if signup_errors:
            error_message = "That signup won't work.<br />Here are some hints:<br /><h5>"

            for key, value in signup_errors.items():
                values = value.split(".")
                for v in values:
                    error_message += v + "<br />"

            messages.error(request, error_message + "</h5>")
            return HttpResponseRedirect(reverse('index'))

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

    if request.method == "POST" and not request.user.is_authenticated:

        username = request.POST['uname']
        password = request.POST['psw']
        keep_log_in = request.POST.get('keep_log_in', None)

        user = authenticate(request, username=username, password=password)

        # if user is not None, then there are no errors
        if user:
            login(request, user)
        else:
            messages.error(request, 'Those are invalid credentials. Please try again.')
            HttpResponseRedirect(reverse('index'))

        if keep_log_in:
            request.session.set_expiry(60 * 60 * 24 * 10) # set expiry for 10 days

        #else, uses the default expiry at browser close

    return HttpResponseRedirect(redirect)

def logout_view(request):
    redirect = request.GET.get('next', reverse('index'))
    logout(request)
    return HttpResponseRedirect(redirect)

@login_required
def send_email_validation(request):
    # send the request
    current_domain = 'localhost:8000'
    message = render_to_string('account/email_verify.html', {
        'username': request.user.username,
        'domain': current_domain,
        'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
        'token': account_activation_token.make_token(request.user),
    })

    send_mail('URSell Email Validation',    #subject
              message,
              'ursell.test@gmail.com', #from
              [request.user.email])  #to

    return HttpResponseRedirect(reverse('index'))

def validate_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Your email is now verified.')
    else:
        return HttpResponse('Activation link is invalid!')
