# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from .views import social_login_callback
from .app_settings import SOCIAL_LOGIN_CALLBACK_URL_PATTERN

# SOCIAL_LOGIN_CALLBACK_URL_PATTERN is the OAuth2 call back url format.
# settings this in Social site which you are using the OAuth2 services.

urlpatterns = [
    url(SOCIAL_LOGIN_CALLBACK_URL_PATTERN, social_login_callback, name='social_login_callback'),
]
