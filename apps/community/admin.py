from django.contrib import admin

from apps.community import Post, Comment, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
