# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20171115_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(default='posts/no_image_available.svg', upload_to=posts.models.unique_post_name),
        ),
    ]
