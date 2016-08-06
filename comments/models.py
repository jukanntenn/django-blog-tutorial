from django.db import models
from django_comments.abstracts import CommentAbstractModel


class CommentWithParent(CommentAbstractModel):
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children',
                               verbose_name='父评论')
