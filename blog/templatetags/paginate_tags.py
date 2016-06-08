from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()


@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    left = 3
    right = 3

    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
    finally:
        if isinstance(page, int):
            object_list = paginator.page(page)
        context['current_page'] = int(page)
        pages = get_pages(context['current_page'], left, right, paginator.num_pages)

    context['article_list'] = object_list
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    context['pages_first'] = pages[0] if pages else 1
    context['pages_last'] = pages[-1] + 1 if pages else 2

    return ''  # 必须加这个，否则首页会显示个None


def get_pages(current_page, left, right, num_pages):
    page = current_page - 1 if current_page == num_pages else current_page

    pages = (
        [i for i in range(page - left + 1, page + 1) if i > 1] +
        [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]
    )
    return pages
