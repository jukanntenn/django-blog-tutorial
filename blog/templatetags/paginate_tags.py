from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()


@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')
    pages = [i + 1 for i in range(paginator.num_pages)]

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages

    context['article_list'] = object_list
    context['paginator'] = paginator
    context['pages'] = pages

    return ''  # 必须加这个，否则首页会显示个None
