from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from config import settinggs

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

    def __str__(self):
        return '%s: %s(%s)' % (self.content_type, self.object_id, self.follow_num)

'''
follow详情
@param {Boolean} is_follow　是否关注
@param {Date} follow_time 关注的时间
@param {Object}　外键关联Follow类
@param {Object} 外键关联，登陆用户
'''
class FollowDetail(models.Model):
    is_follow = models.BooleanField(default = False)
    follow_time = models.DateTimeField(auto_now = True)
    follows = models.ForeignKey(Follow)
    user = models.ForeignKey(settinggs.AUTH_USER_MODEL)

    class Meta:
        ordering = ['-follow_time']

