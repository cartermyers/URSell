from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^validate_email/((?P<user_id>[0-9]+)/)?$', views.validate_email, name='validate_email'),
    #url(r'^$', views.profile, name='profile') #this will be the profile page
                                            #TODO later
]
