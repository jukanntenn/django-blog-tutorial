from django.contrib import admin
from .models import Follow
# Register your models here.

class FollowAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'follow_num')
    search_field = ('object_id')

admin.site.register(Follow, FollowAdmin)
