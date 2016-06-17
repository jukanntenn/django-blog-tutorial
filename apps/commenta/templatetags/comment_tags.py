from django import template
from django.contrib.contenttypes.models import ContentType
from ..forms import CommentForm
from ..models import Comment

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
