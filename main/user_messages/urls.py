from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mailbox, name='mailbox'),
    url(r'^send/$', views.send_user_mail, name='send_user_mail'),
    url(r'^delete_mail/(?P<mail_id>[0-9]+)/$', views.delete_mail, name='delete_mail'),
]
