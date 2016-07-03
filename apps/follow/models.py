from django.db import models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from config import settings


# Create your models here.
# 关注帖子的功能,同时也可以扩展为其他关注的功能

class FollowManager(models.Manager):
    def follow_toggle(self, trigger_user, content_type, object_id):
        obj, followed = self.get_or_create(
                trigger_user=trigger_user,
                content_type=content_type,
                object_id=object_id,
        )

        if not followed:
            obj.delete()
        return obj, followed


class Follow(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    trigger_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed_objects')
    follow_time = models.DateTimeField(auto_now=True)

    # 关注级别：
    # 0：常规：仅有人@我时提醒
    # 1：特别：有人回复此话题时提醒
    level = models.PositiveIntegerField(default=0)

    objects = FollowManager()

    def __str__(self):
        return '%s followed %s' % (self.trigger_user, self.content_object)

    class Meta:
        ordering = ['-follow_time']
