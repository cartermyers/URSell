# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import SentMail, RecieveMail

@login_required
def mailbox(request):

    # get all mailboxes
    sent = SentMail.objects.filter(sender_id=request.user.pk)
    received = RecieveMail.objects.filter(reciever_id=request.user.pk)
    trash = sent.filter(trash=True).union(received.filter(trash=True))

    #now remove all trash objects from sent and received
    sent = sent.difference(trash)
    received = received.difference(trash)

    return render(request, 'user_messages/mailbox.html', {'sent': sent, 'received': received, 'trash': trash})
