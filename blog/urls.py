from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^main/$', views.main, name ='main'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    #url(r'^signin/$', views.signin, name='signin'),
    #url(r'^signout/$', views.signout, name='signout'),
    #url(r'^signin_sent/$', views.signin_sent, name='signin_sent'),
    #url(r'^register/$', views.register, name='register'),

]
