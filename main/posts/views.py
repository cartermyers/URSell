# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Categories, Posts, PostImages

@login_required
def new_post(request):
    """ a view to handle and present the new post form
        post fields include:

        1
        - adtitle (text)
        - type (radio: offering/wanting)
        - price (investigate this input more)
        - NOTE: NAME NEEDED description

        2
        - Image array (NEEDS DIFFERENT NAMES)

        4
        - detail (selection, basically a category) THIS VALUE SHOULD BE THE CATEGORY KEY
        """

    errors = dict()

    # process form here
    if request.method == "POST":

        poster = request.user.pk
        category = request.POST['detail']

        title = request.POST['adtitle']
        price = request.POST['price']
        description = request.POST['description']
        offering = True if request.POST['type'] == 'offering' else False

        new_post = Posts(category=category, poster=poster, title=title, price=price, description=description, offering=offering)
        new_post.save()

        #and save all of the images:
        for image in request.FILES.get_list('images'):
            new_image = PostImages(new_post.pk, image)
            new_image.save()

        # if it's a successful post, redirect to the new page:
        return HttpResponseRedirect(reverse('postpage.html'))


    # render the page with any errors or just a plain form

    categories = Categories.objects.all()
    return render(request, 'posts/post2.html', {'errors': errors, 'categories': categories})

def categories(request):
    return render(request, 'posts/categories.html')

def categories_test(request):
    return render(request, 'posts/categoriestest.html')

def test(request):
    return render(request, 'posts/test.html')
