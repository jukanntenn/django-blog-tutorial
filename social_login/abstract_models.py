#  -*- coding: utf-8 -*-
#
# from django.db import models
#
# from .manager import InnerUserManager
#
#
# class AbstractBaseSiteUser(models.Model):
#     """
#     Abstract model for store the common info of social user and inner user.
#     You can extend the abstract model like this:
#
#     class CustomAbstractSiteUser(AbstractBaseSiteUser):
#         # some extra fields...
#
#         class Meta:
#             abstract = True
#
#     then, and your model in settings.py file:
#     SOCIAL_LOGIN_ABSTRACT_SITEUSER = 'myapp.CustomAbstractSiteUser'
#     """
#     is_social = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True, db_index=True)
#
#     class Meta:
#         abstract = True
#
#
#
#
# # your project's user model must inherit from the following two abstarct model
#
# class AbstractInnerUserAuth(models.Model):
#     user = models.OneToOneField('social_login.SiteUser', related_name='inner_user')
#     objects = InnerUserManager()
#
#     class Meta:
#         abstract = True
#
#
# class AbstractUserInfo(models.Model):
#     user = models.OneToOneField('social_login.SiteUser', related_name='user_info')
#     username = models.CharField(max_length=32)
#     avatar = models.CharField(max_length=255, blank=True)
#
#     class Meta:
#         abstract = True
