# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Mail, SentMail, RecieveMail, send_mail
from account.models import User

@login_required
def send_user_mail(request):

    if request.method =="POST":
        to = request.POST['contact_name']
        subject = request.POST['contact_subject']
        message = request.POST['contact_message']

        try:
            to = User.objects.get(username=to)
        except User.DoesNotExist:
            messages.error(request, "Sorry! There's no user with that username.")
            return HttpResponseRedirect(reverse('messages:mailbox'))

        m = Mail(sender_id=request.user.pk, reciever_id=to.pk, subject=subject, content=message)
        send_mail(m)

    return HttpResponseRedirect(reverse('messages:mailbox'))

@login_required
def mailbox(request):

    # get all mailboxes
    sent = SentMail.objects.filter(sender_id=request.user.pk)
    received = RecieveMail.objects.filter(reciever_id=request.user.pk)
    trash = sent.filter(trash=True).union(received.filter(trash=True))

    #now remove all trash objects from sent and received
    sent = set(sent).difference(set(trash))
    received = set(received).difference(set(trash))

    #now order by time
    sent = sent.order_by('-time')
    received = received.order_by('-time')
    trash = trash.order_by('-time')

    return render(request, 'user_messages/mailbox.html', {'sent': sent, 'received': received, 'trash': trash})

@login_required
def delete_mail(request, mail_id):
    try:
        try:
            mail = SentMail.objects.get(pk=mail_id, sender_id=request.user.pk)
        except SentMail.DoesNotExist:
            mail = RecieveMail.objects.get(pk=mail_id, reciever_id=request.user.pk)

        mail.delete()
    except RecieveMail.DoesNotExist:
        pass

    return HttpResponseRedirect(reverse('messages:mailbox'))
