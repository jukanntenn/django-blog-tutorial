# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
)

# Create your models here.
@python_2_unicode_compatible
class ForumUser(AbstractUser):
    mugshot = models.ImageField('头像', upload_to='/uploads')
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField('生日')
    self_intro = models.TextField('个人简介')
    sign_up_ip = models.GenericIPAddressField('注册时IP')
    last_login_time = models.DateTimeField('最后一次登录时间', auto_now=True)
    last_login_ip = models.GenericIPAddressField('最后一次登录IP')
    website = models.URLField('个人网站', max_length=200)
    github = models.URLField('GitHub主页地址', max_length=200)
    nickname = models.CharField('昵称', max_length=20)
    sector = models.CharField('所在单位', max_length=200)
    position = models.CharField('职位', max_length=40)
    focus_users = models.ManyToManyField('self', verbose_name='关注的人', related_name='focus_users')
    fans = models.ManyToManyField('self', verbose_name='粉丝', related_name='fans')

    def __str__(self):
        return self.user_name
