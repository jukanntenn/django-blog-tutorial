from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.db.models.manager import Manager
from .signals import notify


class NotificationQuerySet(models.QuerySet):
    """定义获取特定通知集的方法
    """

    def read(self):
        return self.filter(unread=False)

    def unread(self):
        return self.filter(unread=True)


class Notifications(models.Model):
    """
    通知。
    格式：<用户X> 在 <帖子> 中回复了你 [内容]
    """
    # 接收通知的用户
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')

    unread = models.BooleanField(default=True)

    # 通知发起者
    actor_content_type = models.ForeignKey(ContentType, related_name='notify_actor')
    actor_object_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    # 通知描述
    verb = models.CharField(max_length=255)
    description = models.TextField()

    # 参与通知的对象，例如帖子
    action_object_content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                                   related_name='notify_action_object')
    action_object_object_id = models.PositiveIntegerField(blank=True, null=True)
    action_object = GenericForeignKey('action_object_content_type', 'action_object_object_id')

    created_time = models.DateTimeField(auto_now_add=True)

    objects = NotificationQuerySet.as_manager()

    class Meta:
        ordering = ['-created_time', ]

    def __str__(self):
        # TO-DO 更好地格式化通知描述
        return self.description

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()


def notification_handler(sender=None, **kwargs):
    recipient = kwargs.pop('recipient')
    verb = kwargs.pop('verb')
    description = kwargs.pop('description')
    action_object = kwargs.pop('action_object')

    created_data = {
        'recipient': recipient,
        'actor_content_type': ContentType.objects.get_for_model(sender),
        'actor_object_id': sender.pk,
        'verb': verb,
        'description': description,
        'action_object': action_object,
    }

    Notifications.objects.create(**created_data)


notify.connect(notification_handler, dispatch_uid='notifications.models.notification')
