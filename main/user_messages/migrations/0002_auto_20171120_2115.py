# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_messages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecieveMail',
        ),
        migrations.RemoveField(
            model_name='sentmail',
            name='sender',
        ),
        migrations.DeleteModel(
            name='SentMail',
        ),
    ]
