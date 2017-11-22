# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import User

import uuid
import os

def unique_post_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)    #this generates a unique id for the filename
    return os.path.join('posts', filename)

class Categories(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title

class Posts(models.Model):
    # all foreign dependencies
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)   #default is unknown category
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default=1)           #default is unknown user    NOTE: in practice, these should never be used

    # own attributes
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #maybe change this type of field later
    description = models.TextField(null=True)
    offering = models.BooleanField(default=True)    #false means they are wanting

    def __str__(self):
        return self.title

# here is a simple model that allows us to store an arbitrary amount of images per post
class PostImages(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    image = models.ImageField(upload_to=unique_post_name)
