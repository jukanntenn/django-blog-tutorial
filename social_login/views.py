# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login

from socialoauth.sites.base import socialsites
from socialoauth.utils import import_oauth_class
from socialoauth.exception import SocialAPIError

from accounts.models import BlogUser

from .models import SocialUser

from .app_settings import (
    SOCIALOAUTH_SITES,
    SOCIAL_LOGIN_DONE_REDIRECT_URL,
    SOCIAL_LOGIN_ERROR_REDIRECT_URL,
)

socialsites.config(SOCIALOAUTH_SITES)


def social_login_callback(request, sitename):
    user = None
    code = request.GET.get('code', None)
    if not code:
        # Maybe user not authorize
        return HttpResponseRedirect(SOCIAL_LOGIN_ERROR_REDIRECT_URL)

    s = socialsites.get_site_object_by_name(sitename)

    try:
        s.get_access_token(code)
    except SocialAPIError:
        # see social_oauth example and docs
        return HttpResponseRedirect(SOCIAL_LOGIN_ERROR_REDIRECT_URL)

    try:
        social_user = SocialUser.objects.get(site_uid=s.uid, site_name=sitename)
        # got user, update username and avatar
        user = social_user.user
        user.nickname = s.name
        user.mugshot = s.avatar
        user.save(update_fields=['nickname', 'mugshot'])

    except SocialUser.DoesNotExist:
        print('-------------------')
        pwd = BlogUser.objects.make_random_password()
        user = BlogUser.objects.create_user(
                username=s.uid,
                password='yxg19940330'
        )
        user.nickname = s.name
        user.mugshot = s.avatar
        user.save()
        SocialUser.objects.create(site_uid=s.uid, site_name=sitename, user=user)
    print(user)
    setattr(user, 'backend', 'likes.auth_backends.CanLikeBackend')
    login(request, user)
    print(user.is_authenticated())

    # set uid in session, then next time, this user will be auto loggin
    # request.session['uid'] = user.pk

    return HttpResponseRedirect(SOCIAL_LOGIN_DONE_REDIRECT_URL)
