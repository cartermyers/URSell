# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)

class Categories(models.Model):
    title = models.CharField(max_length=40) 

