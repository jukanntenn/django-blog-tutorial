# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

from .app_settings import SOCIAL_LOGIN_UID_LENGTH


# def _abstract_siteuser():
#     custom_siteuser = getattr(settings, 'SOCIAL_LOGIN_ABSTRACT_SITEUSER', None)
#     if not custom_siteuser:
#         from .abstract_models import AbstractBaseSiteUser
#         return AbstractBaseSiteUser
#
#     _app, _model = custom_siteuser.split('.')
#     _module = __import__('%s.models' % _app, fromlist=[_model])
#     _model = getattr(_module, _model)
#
#     if not _model._meta.abstract:
#         raise AttributeError("%s must be abstract model" % custom_siteuser)
#     return _model
#
#
#
# class SiteUser(_abstract_siteuser()):
#
#     def __unicode__(self):
#         return '<SiteUser %d>' % self.id


class SocialUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='social_user')
    site_uid = models.CharField(max_length=100)
    site_name = models.CharField(max_length=20)

    class Meta:
        unique_together = (('site_uid', 'site_name'),)
