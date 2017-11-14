# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import User

class Categories(models.Model):
    title = models.CharField(max_length=40)

class Posts(models.Model):
    # all foreign dependencies
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)   #default is unknown category
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default=1)           #default is unknown user    NOTE: in practice, these should never be used

    # own attributes
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #maybe change this type of field later
    description = models.TextField(null=True)

# here is a simple model that allows us to store an arbitrary amount of images per post
class PostImages(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='posts/')
