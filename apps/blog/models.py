# -*- coding: utf-8 -*-
import datetime
import re

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


# Create your models here.
@python_2_unicode_compatible
class ArchivesManager(models.Manager):
    def get_queryset(self):
        return Article.objects.datetimes('pub_date', 'month', order='DESC')


class ArchivesItem(models.Model):
    archives = ArchivesManager()


class ArticleManager(models.Manager):
    def archive(self):
        dates = Article.objects.dates('year', 'month').distinct()
        return dates


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', "已发布"),
    )

    objects = ArchivesManager()

    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    cover = models.URLField('封面图片', default='', blank=True)
    abstract = models.TextField('摘要', max_length=1024, blank=True, null=True, help_text="可选，如若为空将摘取正文的前54个字符")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    pub_date = models.DateTimeField('发表时间', auto_now=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='所属分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True, help_text='标签')

    slug = models.SlugField('slug', unique=True, max_length=100)
    slug.help_text = "Cool URIs don't change"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'article_id': self.pk})

    def get_absolute_url(self):
        return reverse('blog:detail', args=(self.id, self.slug))

    def save(self, *args, **kwargs):
        self.abstract = self.abstract or self.body[:140]
        # auto_now 已经实现了保存时自动修改时间
        # modified = kwargs.pop("modified", True)
        # if modified:
        #     self.last_modified_time = datetime.datetime.utcnow()
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']


class Tag(models.Model):
    name = models.CharField('名称', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('名称', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
