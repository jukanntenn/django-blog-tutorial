from django import template
from django.contrib.contenttypes.models import ContentType
from ..forms import CommentForm
from ..models import Comment
from django.utils.timesince import timesince

register = template.Library()


@register.simple_tag(takes_context=True)
def comment_form(context, obj):
    user = context.get('user')
    form = CommentForm(target_object=obj, user=user)
    return form


@register.simple_tag
def comments(obj):
    return Comment.objects.filter(
            object_id=obj.pk,
            content_type=ContentType.objects.get_for_model(obj),
            parent__isnull=True,
    ).order_by('-created_time')


@register.simple_tag
def comment_count(obj):
    return Comment.objects.filter(
            object_id=obj.pk,
            content_type=ContentType.objects.get_for_model(obj)
    ).count()


@register.filter
def last_comment_by(obj):
    """
    This way make template do extra thing,should be refactored,
    """
    try:
        return Comment.objects.filter(
                object_id=obj.pk,
                content_type=ContentType.objects.get_for_model(obj)
        ).order_by('-modified_time').first().author.username
    except AttributeError:
        return ''


@register.filter
def last_comment_timesince(obj):
    last_comment = Comment.objects.filter(
            object_id=obj.pk,
            content_type=ContentType.objects.get_for_model(obj)
    ).order_by('-modified_time').first()
    return timesince(last_comment.modified_time)
