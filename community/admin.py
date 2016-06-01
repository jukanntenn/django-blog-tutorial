from django.contrib import admin
from community.models import Post, Comment, Reaction
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
