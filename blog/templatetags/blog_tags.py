from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
