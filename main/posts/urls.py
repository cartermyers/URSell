from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories', views.categories, name='categories'),
    url(r'^categories_test', views.categories_test, name='categories_test')
]
