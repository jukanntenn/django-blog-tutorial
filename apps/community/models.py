from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='上次编辑时间', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='发帖人', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签', max_length=50)
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)

    class Meta:
        ordering = ['-published_date', ]
        verbose_name = '帖子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
