# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import User

# TO RUN TESTS ENTER 'python manage.py test <model>'

class UserModelTests(TestCase):

    def test_email_validation(self):
        email = "wrongemail@gmail.com"
        self.IsAssert() # or something

    def test_password_validation(self):
        pass

    def test_user_signup(self):
        # test for same emails
        # test for same usernames
        # test for proper case
        pass
