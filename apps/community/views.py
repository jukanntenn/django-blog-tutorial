from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import PostForm
from .models import Post


class PostCreateView(CreateView):
    template_name = 'community/post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class IndexView(ListView):
    pass


class PostDetailView(DetailView):
    pass
