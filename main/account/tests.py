# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import User

# Whenever Django runs tests, it creates a temporary database just for testing.
# So feel free to insert new data as you please without having to remove it.
# This temporary DB also makes it easy to query.

# TO RUN TESTS ENTER 'python manage.py test <model>'

class UserModelTests(TestCase):

    def test_email_validation(self):
        email = "wrongemail@gmail.com"
        self.assertIs(User.validate_email(email), False)
        email = "@uregina.ca"
        self.assertIs(User.validate_email(email), False)

    def test_pic_name_validation(self):
        pass

    def test_password_validation(self):
        pass

    def test_user_signup(self):
        # test for same emails (error)
        # test for same usernames (error)
        # test for same profile pics (i.e. I can add two users with the same profile pic name)
        # test for different passwords (in psw and psw-repeat)
        # could test password validation, but it's from Django so I trust it
        pass
