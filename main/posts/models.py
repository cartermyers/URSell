# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)

# here is a simple model that allows us to store an arbitrary amount of images per post
class PostImages(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

class Categories(models.Model):
    title = models.CharField(max_length=40)
