# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from account.models import User

class SentMail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None)



# Basically, a copy
class RecieveMail(models.Model):
    pass
