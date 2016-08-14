# -*- coding: utf-8 -*-

from socialoauth.utils import import_oauth_class

from socialoauth.sites.base import socialsites
from .app_settings import (
    SOCIALOAUTH_SITES,
)

socialsites.config(SOCIALOAUTH_SITES)


# add 'social_login.context_processors.social_sites' in TEMPLATE_CONTEXT_PROCESSORS
# then in template, you can get this sites via {% for s in social_sites %} ... {% endfor %}
# Don't worry about the performance,
# `social_sites` is a lazy object, it readly called just access the `social_sites`


# def social_sites(request):
#     def _social_sites():
#         def make_site(s):
#             s = import_oauth_class(s)()
#             return {
#                 'site_name': s.site_name,
#                 'site_name_zh': s.site_name_zh,
#                 'authorize_url': s.authorize_url,
#             }
#
#         return [make_site(s) for s in socialsites.list_sites()]
#
#     return {'social_sites': LazyList(_social_sites)}

def social_sites(request):
    def make_site(s):
        s = import_oauth_class(s)()
        return s.authorize_url

    return {s.split('.')[-2]: make_site(s) for s in socialsites.list_sites_class()}
