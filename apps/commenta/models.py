from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    body = models.TextField("评论内容")
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    parent = models.ForeignKey('self', null=True, related_name='child_comments')

    def __str__(self):
        return self.body[:20]
