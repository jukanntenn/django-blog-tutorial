# coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes admin
"""
from django.contrib import admin
from .models import Likes, LikesDetail


class LikesAdmin(admin.ModelAdmin):
    """likes admin"""
    list_display = ('id', 'content_type', 'object_id', 'likes_num')
    search_fields = ('object_id',)


class LikesDetailAdmin(admin.ModelAdmin):
    """likes detaile admin"""
    list_display = ('id', 'likes', 'user', 'is_like', 'pub_date')
    # filter date
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


admin.site.register(Likes, LikesAdmin)
admin.site.register(LikesDetail, LikesDetailAdmin)
