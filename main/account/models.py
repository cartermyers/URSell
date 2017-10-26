# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """See https://docs.djangoproject.com/en/1.11/topics/auth/customizing/ for all fields/attributes included in the superuser"""

    # CLASS FIELDS
    # These are the attributes in the database
    validated_email = models.BooleanField(default=False)

    # CLASS METHODS
    # These are class functions
    def __str__(self):
        """Default text representation of a user"""
        return self.get_username()
