# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mailbox(request):
    # get type of mailbox:
    box = request.GET.get('box', None)

    if box == 'sent':
        pass
        #get sent mails
    elif box == 'received':
        pass
        # get received mail
    else:
        pass
        #put some kind of error here

    return render(request, 'user_messages/mailbox_test.html')
