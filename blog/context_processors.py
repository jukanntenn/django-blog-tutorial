from django.db.models.aggregates import Count
from .models import Category, Article


def sidebar(request):
    category_list = Category.objects.filter(article__status='p').annotate(num_articles=Count('article')).filter(
            num_articles__gt=0)
    recent_articles = Article.objects.filter(status='p')[:5]
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    return {
        'category_list': category_list,
        'recent_articles': recent_articles,
        'dates': dates,
    }
