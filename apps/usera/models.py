from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CommunityUser(AbstractUser):
    """
    AbstractUser 已含有 username、password、first_name、last_name、email、is_staff、is_active、date_joined、last_login 属性
    """
    sign_up_ip = models.GenericIPAddressField('注册时IP', null=True)
    last_login_ip = models.GenericIPAddressField('最后一次登录IP', null=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', '帅哥'),
        ('F', '美女'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField('昵称', max_length=50, blank=True)
    mugshot = models.ImageField('头像', upload_to='/uploads', blank=True)  # 不要给CharField相关的属性设置null=True
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField('生日', blank=True, null=True)
    self_intro = models.TextField('个人简介', blank=True)
    website = models.URLField('个人网站', max_length=200, blank=True)
    github = models.URLField('GitHub主页地址', max_length=200, blank=True)
    sector = models.CharField('所在公司或学校', max_length=200, blank=True)
    occupation = models.CharField('职业', max_length=50, blank=True)
    concerned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='关注的人',
                                             related_name='concerned_users')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='粉丝', related_name='followers')
