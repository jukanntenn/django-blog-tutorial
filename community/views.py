from django.shortcuts import render
from django.views.generic import FormView
from community.forms import PostForm, ReplyForm


# Create your views here.
class PostCreateView(FormView):
    template_name = 'community/post_create.html'
    form_class = PostForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PostCreateView, self).form_valid(form)


class ReplyCreateView(FormView):
    template_name = ''
    form_class = ReplyForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(ReplyCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ReplyCreateView, self).form_valid(form)
