from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from config import settings

# Create your models here.
# 关注帖子的功能,同时也可以扩展为其他关注的功能
'''
Follow类，使用ContentType框架，默认follow数量为０
'''
class Follow(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    follow_num = models.IntegerField(default = 0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    follow_time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return '%s: %s(%s)' % (self.content_type, self.object_id, self.follow_num)

    class Meta:
        ordering = ['-follow_time']
