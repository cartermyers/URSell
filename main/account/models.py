# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import password_validation

import re

class User(AbstractUser):
    """See https://docs.djangoproject.com/en/1.11/topics/auth/customizing/ for all fields/attributes included in the superuser"""

    # CLASS FIELDS
    # These are the attributes in the database
    validated_email = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='account/', default='account/unknownuser.jpg')

    # CLASS METHODS
    # These are class functions
    def __str__(self):
        """Default text representation of a user"""
        return self.get_username()

    @staticmethod
    def validate_email(email):
        return re.match(r"\S{3,}@uregina.ca$", email)

    @staticmethod
    def validate_signup(email, password, password_repeat, username, pic):
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
            signup_errors['email'] = "Email is already registered"
        except User.DoesNotExist:
            pass

        # validate the password:
        try:
            password_validation.validate_password(password)
        except password_validation.ValidationError:
            signup_errors['password'] = password_validation.password_validators_help_texts()

        # check if passwords match
        if password != password_repeat:
            signup_errors['password'] = "Your passwords did not match."


        #unique username
        try:
            User.objects.get(username=username)
            signup_errors['username'] = "Username already exists."
        except User.DoesNotExist:
            pass

        #       check if a picture with the same name already exists:

        try:
            count = 1
            old = User.objects.get(profile_pic= "account/" + pic.name)
            while old:
                pic.name = pic.name + "(" + str(count) + ")"
                count += 1
                old = User.objects.get(profile_pic="account/" + pic.name)
        except User.DoesNotExist:
                # else, we are fine
                pass

        return signup_errors if signup_errors else None
