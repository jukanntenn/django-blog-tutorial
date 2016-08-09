# -*- coding: utf-8 -*-

from django.conf import settings

# the following three are REQUIRED in django.conf.settings
SOCIALOAUTH_SITES = settings.SOCIALOAUTH_SITES
SOCIAL_LOGIN_ERROR_REDIRECT_URL = settings.SOCIAL_LOGIN_ERROR_REDIRECT_URL


SOCIAL_LOGIN_UID_LENGTH = getattr(settings, 'SOCIAL_LOGIN_UID_LENGTH', 255)
SOCIAL_LOGIN_ENABLE_ADMIN = getattr(settings, 'SOCIAL_LOGIN_ENABLE_ADMIN', True)


SOCIAL_LOGIN_CALLBACK_URL_PATTERN = getattr(settings,
                                            'SOCIAL_LOGIN_CALLBACK_URL_PATTERN',
                                            r'^account/oauth/(?P<sitename>\w+)/?$'
                                            )

SOCIAL_LOGIN_DONE_REDIRECT_URL = getattr(settings,
                                         'SOCIAL_LOGIN_DONE_REDIRECT_URL',
                                         '/'
                                         )

SOCIAL_LOGIN_SITEUSER_SELECT_RELATED = getattr(settings,
                                               'SOCIAL_LOGIN_SITEUSER_SELECT_RELATED',
                                               ('user_info',)
                                               )