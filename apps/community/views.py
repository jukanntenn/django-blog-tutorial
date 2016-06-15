from django.views.generic import FormView, ListView, DetailView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post
import markdown2


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'community/post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class IndexView(ListView):
    model = Post
    template_name = "community/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        post_list = Post.objects.all()
        for post in post_list:
            post.body = markdown2.markdown(post.body, extras=['fenced-code-blocks'], )
        return post_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'community/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj
