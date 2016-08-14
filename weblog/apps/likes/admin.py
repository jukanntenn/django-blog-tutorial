from django.contrib import admin

from .models import Like


admin.site.register(
    Like,
    raw_id_fields=["sender"],
    list_filter=["timestamp"],
    list_display=["sender", "receiver", "timestamp"],
    search_fields=["sender__username", "sender__email"]
)
