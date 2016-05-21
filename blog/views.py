from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Article, Category
import markdown2


# Create your views here.
class IndexView(ListView):  # 首页视图
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    slug_field = 'id'

    def get_object(self):
        object = super(ArticleDetailView, self).get_object()
        object.body = markdown2.markdown(object.body)
        return object


class CategoryView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'])
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)
