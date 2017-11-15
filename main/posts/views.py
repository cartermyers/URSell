# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

        new_post = Posts(category, poster, title, price, description, offering)
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

def ads(request, category):
    if category:
        # get posts with category key
        post_list = get_object_or_404(Posts, category=category)
    else:
        # get all posts
        post_list = Posts.objects.all()

    items_per_page = 10

    page_list = Paginator(post_list, items_per_page)

    """ Here is some code from https://docs.djangoproject.com/en/1.11/topics/pagination/ """
    current_page = request.GET.get('page', None)
    try:
        posts = page_list.page(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = page_list.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = page_list.page(page_list.num_pages)

    return render(request, 'posts/ads.html', {'posts': posts})


def categories(request):
    return render(request, 'posts/categories.html')

def categories_test(request):
    return render(request, 'posts/categoriestest.html')

def test(request):
    return render(request, 'posts/test.html')
