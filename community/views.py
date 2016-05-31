from django.shortcuts import render
from django.views import generic

from community.models import Post, Comment

import markdown2
# Create your views here.

class IndexView(generic.ListView):
    model = Post
    template_name = "community/index.html"
    context_object_name = "post_list"

    # def get_queryset(self):
    #     post_list = Post.objects.filter(is_published=True)
    #     for post in post_list:
    #         post.body = markdown2.markdown(post.body, extras=['fenced-code-blocks'], )
    #     return post_list

    def get_context_data(self, **kwargs):
        kwargs['post_list'] = Post.objects.all().order_by('-last_modified_time')
        return super(IndexView, self).get_context_data(**kwargs)

class PostDetailView(generic.DetailView):
    pass