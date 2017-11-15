from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ads/((?P<category>[0-9]+)/)?$', views.ads, name='ads'),
    url(r'^newpost/$', views.new_post, name='newpost'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories_test/$', views.categories_test, name='categories_test'),
    url(r'^test/$', views.test, name='test'), #temporary test page
]
