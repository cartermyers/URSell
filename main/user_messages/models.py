# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from account.models import User

# an abstract class for mailboxes
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='+')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='+')

    time = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    trash = models.BooleanField(default=False)

    def __str__(self):
        return "From: " + self.sender.username + "; To: " + self.reciever.username + "; Title: " + self.subject

    def delete(self, *args, **kwargs):
        if self.trash:
            super(Mail, self).delete(*args, **kwargs)
        else:
            self.trash = True
            super(Mail, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class SentMail(Mail):
    pass

# Basically, a copy
class RecieveMail(Mail):
    pass

def send_notification(mail):
    r = RecieveMail(sender_id=mail.sender_id, reciever_id=mail.reciever_id, subject=mail.subject, content=mail.content)
    r.save()
    # this function handles the received box as well:
    user = User.objects.get(pk=mail.reciever_id)
    user.send_email_notification(mail.subject, mail.content)

# whenever we send mail from user to user, save two copies:
def send_mail(mail):
    s = SentMail(sender_id=mail.sender_id, reciever_id=mail.reciever_id, subject=mail.subject, content=mail.content)
    s.save()
    #this handles the received part
    send_notification(mail)
