from django import template
from django.contrib.contenttypes.models import ContentType
from ..forms import SgsCommentForm
from ..models import SgsComment

register = template.Library()


@register.simple_tag(takes_context=True)
def comment_form(context, obj):
    user = context.get('user')
    form = SgsCommentForm(obj=obj, user=user)
    return form


@register.simple_tag
def comments(obj):
    return SgsComment.objects.filter(
            object_id=obj.pk,
            content_type=ContentType.objects.get_for_model(obj),
            parent__isnull=True,
    ).order_by('-created')


@register.simple_tag
def comment_count(obj):
    return SgsComment.objects.filter(
            object_id=obj.pk,
            content_type=ContentType.objects.get_for_model(obj)
    ).count()
