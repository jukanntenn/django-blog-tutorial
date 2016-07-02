from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.filter
def ctype_id(obj):
    return ContentType.objects.get_for_model(obj).pk
