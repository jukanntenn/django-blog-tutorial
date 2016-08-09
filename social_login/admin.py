# -*- coding: utf-8 -*-
# from .app_settings import SOCIAL_LOGIN_ENABLE_ADMIN
from django.contrib import admin
from .models import SocialUser

# if SOCIAL_LOGIN_ENABLE_ADMIN:
#     from django.contrib import admin
#     from .models import SiteUser
#
#     class SiteUserAdmin(admin.ModelAdmin):
#         list_display = ('id', 'Username', 'Avatar', 'is_social', 'is_active',
#                         'date_joined', 'SiteId')
#         list_filter = ('is_social',)
#
#         def Username(self, obj):
#             return obj.user_info.username
#
#         def Avatar(self, obj):
#             return '<img src="%s" />' % obj.user_info.avatar
#         Avatar.allow_tags = True
#
#         def SiteId(self, obj):
#             #return SocialUser.objects.get(id=obj.id).site_id
#             return obj.social_user.site_id


admin.site.register(SocialUser)
