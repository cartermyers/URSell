# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from account.models import User

# an abstract class for mailboxes
class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='+')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='+')

    # time
    subject = models.CharField(max_length=255)
    content = models.TextField()
    trash = models.BooleanField(default=False)

    class Meta:
        abstract = True

class SentMail(Mail):
    pass

# Basically, a copy
class RecieveMail(Mail):
    pass
