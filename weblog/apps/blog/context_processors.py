from django.db.models.aggregates import Count
from .models import Category, Article, Tag


def sidebar(request):
    category_list = Category.objects.filter(article__status='p').annotate(num_articles=Count('article')).filter(
        num_articles__gt=0)
    recent_articles = Article.objects.filter(status='p')[:5]
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    tag_list = Tag.objects.filter(article__status='p').annotate(num_articles=Count('article')).filter(
        num_articles__gt=0)
    return {
        'category_list': category_list,
        'recent_articles': recent_articles,
        'dates': dates,
        'tag_list': tag_list
    }

