from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    body = models.TextField(verbose_name='内容')
    published_date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='上次编辑时间', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='发起者')
    collected_by = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='收藏的用户',
                                          related_name='collected_users')
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='赞过的用户', related_name='liked_users')
    tags = models.ManyToManyField('Tag', verbose_name='标签', max_length=50)
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)

    class Meta:
        ordering = ['-published_date', ]
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    watched_by = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Comment(models.Model):
    body = models.TextField()
    comment_for = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['created_at', ]
        abstract = True

    def __str__(self):
        return self.body[:20]
