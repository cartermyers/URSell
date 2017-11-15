# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import password_validation
from django.core.mail import send_mail

# from main.global_func import unique_file_path

import re


import uuid
import os

def unique_profile_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)    #this generates a unique id for the filename
    return os.path.join('account', filename)

class User(AbstractUser):
    """See https://docs.djangoproject.com/en/1.11/topics/auth/customizing/ for all fields/attributes included in the superuser"""

    # CLASS FIELDS
    # These are the attributes in the database
    validated_email = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=unique_profile_name, default='account/user-sidebar.png')

    # CLASS METHODS
    # These are class functions
    def __str__(self):
        """Default text representation of a user"""
        return self.get_username()

    @staticmethod
    def validate_email(email):
        return True if re.match(r"\S{3,}@uregina.ca$", email) else False

    @staticmethod
    def validate_pic_name(pic_name):
        try:
            count = 1
            old = User.objects.get(profile_pic="account/" + pic_name)
            name = pic_name.split('.')
            extension = '.' + name.pop(-1)
            while old:
                # do some fancy logic to change the file name:
                # use a new file name for the user
                pic_name = "".join(name) + str(count) + extension
                old = User.objects.get(profile_pic="account/" + pic_name)
                count += 1
        except User.DoesNotExist:
                # else, we are fine
                return pic_name

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

        # check if passwords match
        if password != password_repeat:
            signup_errors['password'] = ["Your passwords did not match."]

        # validate the password:
        # NOTE: it is intentional that it can possibly overwrite the other key
        # it doesn't matter if the passwords match if it is not valid
        try:
            password_validation.validate_password(password)
        except password_validation.ValidationError:
            signup_errors['password'] = password_validation.password_validators_help_texts()

        #unique username
        try:
            User.objects.get(username=username)
            signup_errors['username'] = "Username already exists."
        except User.DoesNotExist:
            pass

        # check if a picture with the same name already exists:
        if pic:
            pic.name = User.validate_pic_name(pic.name)

        return signup_errors if signup_errors else None

    def send_validation_email(self):
        #the url that will process the validation
        # NOTE: this needs to be reviewed
        validation_url = '<a>localhost:8000/account/validate_email/' + str(self.pk) +'/</a>'

        send_mail('URSell Email Validation',    #subject
                  'Please validate your email by selecting the following link: ' + validation_url,  #message
                  'ursell.test@gmail.com', #from
                  [self.email])  #to
