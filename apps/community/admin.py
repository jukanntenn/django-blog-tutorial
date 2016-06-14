from django.contrib import admin

from .models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)
