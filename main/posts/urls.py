from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.post_page, name='post'),
    url(r'^comment/(?P<post_id>[0-9]+)/$', views.comment, name='comment'),
    url(r'^ads/((?P<category>[0-9]+)/)?$', views.ads, name='ads'),
    url(r'^newpost/$', views.new_post, name='newpost'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories_test/$', views.categories_test, name='categories_test'),
    url(r'^test/$', views.test, name='test'), #temporary test page
]
