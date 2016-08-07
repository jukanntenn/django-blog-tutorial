from django.db import models
from django_comments.abstracts import CommentAbstractModel

from .utils import parse_mention


class CommentWithParent(CommentAbstractModel):
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children',
                               verbose_name='父评论')


# temp for receiver
from django.dispatch import receiver

from notifications.signals import notify
from django_comments.signals import comment_was_posted

from likes.signals import object_liked
from likes.models import Like


@receiver(object_liked, sender=Like)
def like_handler(sender, **kwargs):
    like = kwargs.pop('like')
    request = kwargs.pop('request')

    send_data = {
        'recipient': like.receiver.user,
        'sender': like.sender,
        'verb': "赞了",
        'action_object': like.receiver.content_object,
        'target': like.receiver,
        'description': '',
        'timestamp': like.timestamp,
        'level': 'info',
    }
    notify.send(**send_data)


@receiver(comment_was_posted, sender=CommentWithParent)
def mention_handler(sender, **kwargs):
    comment = kwargs.pop('comment')
    request = kwargs.pop('request')

    user = parse_mention(comment.comment)
    if user:
        send_data = {
            'recipient': user,
            'sender': comment.user,
            'verb': "@了",
            'action_object': comment.content_object,
            'target': comment,
            'description': '',
            'timestamp': comment.submit_date,
            'level': 'info',
        }

        notify.send(**send_data)
