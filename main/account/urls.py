from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    #url(r'^$', views.profile, name='profile') #this will be the profile page
                                            #TODO later
]
