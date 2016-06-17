# coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes app
"""
# from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes import generic
from config import settings


# likes number model
class Likes(models.Model):
    # content type
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
            ct_field="content_type",
            fk_field="object_id"
    )
    # content_object = generic.GenericForeignKey('content_type', 'object_id')

    # likes number
    likes_num = models.IntegerField(default=0)

    def __str__(self):
        return '%s:%s(%s)' % (self.content_type, self.object_id, self.likes_num)


# likes detail recode
class LikesDetail(models.Model):
    likes = models.ForeignKey(Likes)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_like = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
