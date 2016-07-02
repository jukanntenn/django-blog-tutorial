from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class LikeManager(models.Manager):
    def like_toggle(self, trigger_user, content_type, object_id):
        obj, liked = self.get_or_create(
                trigger_user=trigger_user,
                content_type=content_type,
                object_id=object_id,
        )

        if not liked:
            obj.delete()
        return obj, liked


class Like(models.Model):
    trigger_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='liked_objects')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    created_time = models.DateTimeField(auto_now_add=True)
    objects = LikeManager()

    class Meta:
        unique_together = ('trigger_user', 'content_type', 'object_id')

    def __str__(self):
        return '{} likes {}'.format(self.trigger_user, self.content_object)
