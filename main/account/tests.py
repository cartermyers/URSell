# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import User

# TO RUN TESTS ENTER 'python manage.py test <model>'

class UserModelTests(TestCase):

    def test_email_signup(self):
        email = "wrongemail@gmail.com"
        User.
        
