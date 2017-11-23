# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Categories, Posts, PostImages, Comments
from main.views import image_validation
from user_messages.models import Mail


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
    categories = Categories.objects.all()

    # process form here
    if request.method == "POST":

        # VALIDATE ALL FIELDS

        poster = request.user.pk
        category = request.POST['detail']
        title = request.POST['adtitle']

        try:
            price = float(request.POST['price'])
        except ValueError:
            # send error message to post form
            errors['price'] = 'Please enter a valid price.'

        description = request.POST['description']
        offering = True if request.POST['type'] == 'offering' else False

        files = []
        if request.FILES.get('files', None):
            files = request.FILES.getlist('files')
            # number of images
            if len(files) > 5:
                errors['images'] = "You can only upload up to 5 pictures per post."
            elif not image_validation(files):
                # image extensions
                errors['images'] = 'You can only upload image file types.'

        if errors:
            return render(request, 'posts/post2.html', {'errors': errors, 'categories': categories})

        # SAVE TO DB

        new_post = Posts(category_id=category, poster_id=poster, title=title, price=price, description=description, offering=offering)
        new_post.save()

        #and save all of the images:
        if files:
            for image in files:
                new_image = PostImages(post_id=new_post.pk, image=image)
                new_image.save()
        # or just save one default image if no uploads
        else:
            new_image = PostImages(post_id=new_post.pk)
            new_image.save()

        return HttpResponseRedirect(reverse('index'))

    # render the page with any errors or just a plain form
    return render(request, 'posts/post2.html', {'errors': errors, 'categories': categories})

def ads(request, category):

    if category:
        # get posts with category key
        post_list = Posts.objects.filter(category=category)
    else:
        # get all posts
        post_list = Posts.objects.all()

    search = request.GET.get('search', '')
    post_list = post_list.filter(Q(title__icontains=search) | Q(description__icontains=search))

    items_per_page = 8

    page_list = Paginator(post_list, items_per_page)

    """ Here is some code from https://docs.djangoproject.com/en/1.11/topics/pagination/ """
    current_page = request.GET.get('page', None)
    try:
        posts = page_list.page(current_page)
        current_page = int(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = page_list.page(1)
        current_page = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = page_list.page(page_list.num_pages)
        current_page = page_list.num_pages

    # do some calculations to find a number of next pages
    start_page = max(0, current_page - 3)
    end_page = min(page_list.num_pages, current_page + 3)
    page_range = range(start_page + 1, end_page + 1)

    return render(request, 'posts/ads.html', {'posts': posts, 'current_page': current_page, 'page_range': page_range})

@login_required
def comment(request, post_id):

    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        # process form
        comment = request.POST['comment']
        c = Comments(post_id=post_id, user_id=request.user.pk, text=comment)
        c.save()

        # send notification/message
        subject = request.user.username + " just commented on your post."
        message = request.user.username + ' commented on your post titled "' + post.title + '". They said "' + comment + '". Go check it out!'

        request.user.send_notification(subject, message)

    return HttpResponseRedirect(reverse('posts:post', kwargs={'post_id': post_id}))


def post_page(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    return render(request, 'posts/item.html', {'post': post})

def categories(request):
    categories = Categories.objects.all().order_by('-pk')

    return render(request, 'posts/categories.html', {'categories': categories})


def test(request):
    return render(request, 'posts/test.html')
