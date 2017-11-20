# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def mailbox(request):
    return render(request, 'user_messages/mailbox_test.html')
