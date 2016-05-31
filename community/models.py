from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from blog.models import Article
from usera.models import ForumUser

# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=100)
    body = models.TextField(verbose_name=u'内容')
    published_time = models.DateTimeField(verbose_name=u'发表时间', auto_now_add=True)
    last_modified_time = models.DateTimeField(verbose_name=u'上次修改时间', auto_now=True)
    author = models.ForeignKey(ForumUser, verbose_name=u'发起者')
    collected_by = models.ForeignKey(ForumUser, verbose_name=u'收藏的用户', related_name='collected_user',
                                     related_query_name='collected_by')
    praised_by = models.ForeignKey(ForumUser,verbose_name=u'赞过的用户', related_query_name='praised_user', related_name='praised_user')
    topic = models.CharField(verbose_name=u'话题', max_length=20, blank=True, null=True)
    views = models.PositiveIntegerField(verbose_name=u'浏览量', default=0)
    ups = models.PositiveIntegerField(verbose_name=u'点赞数', default=0)
    is_page = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    comments_allow = models.BooleanField(default=True)
    attachment = models.FileField(verbose_name=u'附件', upload_to='attachments', null=True, blank=True)

    class Meta:
        ordering = ['-published_time', ]
        verbose_name_plural = u'Post XX'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title is None or self.title == '':
            self.title = self.body[:20]

        super(Post, self).save(*args, **kwargs)


class CommentManager(models.Manager):
    def get_queryset(self):
        return super(CommentManager, self).get_queryset().filter(is_published=True)

@python_2_unicode_compatible
class BaseComment(models.Model):
    text = models.TextField()
    comment_for = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['created_at',]
        abstract = True

    def __str__(self):
        return self.text

class Comment(BaseComment):
    created_by = models.ForeignKey(ForumUser, unique=False, blank=True, null=True, related_name='comment_user')
    is_spam = models.BooleanField(default=False)
    is_published = models.NullBooleanField(default=True, blank=True, null=True)

    objects = CommentManager()

    def get_absolutu_url(self):
        return reversed('community_comment_details', args=[self.id,])

    def save(self, *args, **kwargs):
        if self.is_spam:
            self.is_publised = True
        super(Comment, self).save(*args, **kwargs)

class Reaction(BaseComment):
    """
    Reactions from various social media sites
    """
    reaction_id = models.CharField(max_length=200, primary_key=True)
    source = models.CharField(max_length=200)
    profile_image = models.URLField(blank=True, null=True)