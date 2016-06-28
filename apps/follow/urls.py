# coding: utf-8
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^follow_state/$', views.follow_state, name = 'follow_state'),
    url(r'^follow_nums/$', views.follow_nums, name = 'follow_nums'),
]
