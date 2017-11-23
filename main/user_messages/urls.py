from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mailbox, name='mailbox'),
    url(r'^send/$', views.send_user_mail, name='send_user_mail'),
]
