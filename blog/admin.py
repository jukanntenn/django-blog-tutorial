from django.contrib import admin

# Register your models here.
from blog.models import Article, Category, Tag
from notifications.models import Notification

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
