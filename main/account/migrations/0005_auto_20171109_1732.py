# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20171106_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='account/user-sidebar.png', upload_to='account/'),
        ),
    ]
