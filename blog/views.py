from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView

import markdown2

from .models import Article, Category, Tag


class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object(queryset=None)
        obj.viewed()
        return obj


class CategoryView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category_id'], status='p')


class TagView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(tags=self.kwargs['tag_id'], status='p')


class ArchiveView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArchiveView, self).get_context_data(**kwargs)
