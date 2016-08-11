from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic import TemplateView

import markdown2

from .models import Article, Category, Tag


class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class BlogView(ListView):
    template_name = "blog/blog.html"

    def get_queryset(self):
        return Article.objects.filter(status='p')


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


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


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    make_object_list = True
    context_object_name = 'article_list'
    template_name = 'blog/index.html'


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "created_time"
    context_object_name = 'article_list'
    template_name = 'blog/index.html'
    month_format = '%m'
