from django.db import models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from config import settings


# Create your models here.
# 关注帖子的功能,同时也可以扩展为其他关注的功能
class Follow(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed_objects')
    follow_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s followed %s' % (self.user, self.content_object)

    class Meta:
        ordering = ['-follow_time']
