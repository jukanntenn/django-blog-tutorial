from django.db import models

# Create your models here.
#关注帖子的功能,同时也可以扩展为其他关注的功能
class FollowArticle(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    followed_time = models.DateTimeField('关注时间',auto_now=True) #关注时间
    user_id = models.IntegerField('关注的用户ID',default=1)