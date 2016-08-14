#  -*- coding: utf-8 -*-
#
# from django.db import models
#
#
# class BaseManager(models.Manager):
#     def create(self, is_social, **kwargs):
#         if 'user' not in kwargs and 'user_id' not in kwargs:
#             siteuser_model = models.get_model('social_login', 'SiteUser')
#             user = siteuser_model.objects.create(is_social=is_social)
#             kwargs['user_id'] = user.id
#
#         return super(BaseManager, self).create(**kwargs)
#
#
#
# class SocialUserManager(BaseManager):
#     def create(self, **kwargs):
#         return super(SocialUserManager, self).create(True, **kwargs)
#
#
# class InnerUserManager(BaseManager):
#     def create(self, **kwargs):
#         return super(InnerUserManager, self).create(False, **kwargs)
        
