# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import password_validation
from django.core.mail import send_mail
from django.utils.encoding import python_2_unicode_compatible

from main.views import image_validation

import re

import uuid
import os

def unique_profile_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)    #this generates a unique id for the filename
    return os.path.join('account', filename)

@python_2_unicode_compatible
class User(AbstractUser):
    """See https://docs.djangoproject.com/en/1.11/topics/auth/customizing/ for all fields/attributes included in the superuser"""

    # CLASS FIELDS
    # These are the attributes in the database
    validated_email = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=unique_profile_name, default='account/user-sidebar.png')
    email_notifications = models.BooleanField(default=False)

    # CLASS METHODS
    # These are class functions
    def __str__(self):
        """Default text representation of a user"""
        return self.get_username()

    @staticmethod
    def validate_email(email):
        return True if re.match(r"\S{3,}@uregina.ca$", email) else False

    @staticmethod
    def validate_signup(email, password, password_repeat, username, profile_pic):
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

        signup_errors = dict()

        # ---- email ----

        # u of r email
        if not User.validate_email(email):
           signup_errors['email'] = "Must be a valid University of Regina email."

        # reject the email if it already is registered
        try:
            User.objects.get(email=email)
            signup_errors['email'] = "That email is already registered."
        except User.DoesNotExist:
            pass

        # check if passwords match
        if password != password_repeat:
            signup_errors['password'] = "Your passwords did not match."

        # validate the password:
        # NOTE: it is intentional that it can possibly overwrite the other key
        # it doesn't matter if the passwords match if it is not valid
        try:
            password_validation.validate_password(password)
        except password_validation.ValidationError:
            signup_errors['password'] = " ".join(password_validation.password_validators_help_texts())

        #unique username
        try:
            User.objects.get(username=username)
            signup_errors['username'] = "That username already exists."
        except User.DoesNotExist:
            pass

        # profile pic:
        if profile_pic and not image_validation([profile_pic]):
            signup_errors['pic'] = 'You can only upload image file types.'

        return signup_errors if signup_errors else None

    def send_email_notification(self, subject, message):
        if self.validated_email and self.email_notifications:
            send_mail('URSale: ' + subject,    #subject
                      message,
                      'donotreply.ursale@gmail.com', #from
                      [self.email])  #to
