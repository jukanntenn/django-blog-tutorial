from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Like

register = template.Library()


@register.filter
def ctype_id(obj):
    return ContentType.objects.get_for_model(obj).pk


@register.simple_tag
def who_likes(obj):
    return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
    ).order_by('-created_time')


@register.filter
def likes_count(obj):
    return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
    ).count()


@register.simple_tag(takes_context=True)
def is_liked(context, obj):
    return Like.objects.filter(
            trigger_user=context['request'].user,
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
    ).exists()
