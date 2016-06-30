# coding: utf-8
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^follow/(?P<pk>\d+)/$', views.follow_change, name = 'follow_change'),
]
