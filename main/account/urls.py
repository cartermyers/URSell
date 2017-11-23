from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^validate_email/$', views.send_email_validation, name='send_validate_email'),
    url(r'^validate_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.validate_email, name='validate_email'),
    url(r'^$', views.profile, name='myprofile'), #this is a logged in user's profile page
    url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]
