# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_categories_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]