from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ForumUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
    )
    mugshot = models.ImageField('头像', upload_to='/uploads')
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField('生日', blank=True, null=True)
    self_intro = models.TextField('个人简介', blank=True, null=True)
    sign_up_ip = models.GenericIPAddressField('注册时IP')
    last_login_time = models.DateTimeField('最后一次登录时间', auto_now=True)
    last_login_ip = models.GenericIPAddressField('最后一次登录IP')
    website = models.URLField('个人网站', max_length=200, blank=True, null=True)
    github = models.URLField('GitHub主页地址', max_length=200, blank=True, null=True)
    nickname = models.CharField('昵称', max_length=20, blank=True, null=True)
    sector = models.CharField('所在单位', max_length=200, blank=True, null=True)
    position = models.CharField('职位', max_length=40, blank=True, null=True)
    focus_users = models.ManyToManyField('self', verbose_name='关注的人', related_name='focus_users', null=True)
    fans = models.ManyToManyField('self', verbose_name='粉丝', related_name='fans', null=True)

    def __str__(self):
        return self.user_name
