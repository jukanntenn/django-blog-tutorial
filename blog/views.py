from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView

import markdown2

from .models import Article, ArticleComment, Category, Tag
from .forms import ArticleCommentForm


class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.annotate(num_comments=Count('comments'))


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    pk_url_kwarg = 'article_id'


class CategoryView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category_id'], status='p').annotate(
                num_comments=Count('comments'))


class TagView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.filter(tags=self.kwargs['tag_id'], status='p').annotate(num_comments=Count('comments'))


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


# 第五周新增
class CommentPostView(FormView):
    form_class = ArticleCommentForm
    template_name = 'blog/detail.html'

    def form_valid(self, form):
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        comment = form.save(commit=False)
        comment.article = target_article
        comment.save()
        self.success_url = target_article.get_absolute_url()
        return redirect(self.success_url)

    def form_invalid(self, form):
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        return render(self.request, 'blog/detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.blogcomment_set.all(),
        })
