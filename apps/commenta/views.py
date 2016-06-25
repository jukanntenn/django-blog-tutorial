from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from apps.notifications.signals import notify

from .forms import CommentForm
from .models import Comment


# Create your views here.

class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = CommentForm
    model = Comment
    content_object = None
    parent_comment = None
    object = None
    template_name = 'community/detail.html'

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        kwargs.update({
            "target_object": self.content_object,
            "request": self.request,
            "user": self.request.user,
            "parent": self.parent_comment,
        })
        return kwargs

    def post(self, request, *args, **kwargs):
        ctype_pk = self.request.POST.get('content_type_id')
        object_pk = self.request.POST.get("object_pk")
        content_type = get_object_or_404(ContentType, pk=int(ctype_pk))
        self.content_object = content_type.get_object_for_this_type(pk=int(object_pk))
        try:
            self.parent_comment = Comment.objects.get(id=self.kwargs.get("parent_id"))
        except Comment.DoesNotExist:
            self.parent_comment = None
        return super(CommentCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        description = '用户 {user} 在你发表的帖子 {post} 中回复了你：{comment}' \
            .format(user=self.request.user.username, post=self.content_object.title, comment=form.instance.body[:50])
        notify.send(self.request.user, recipient=self.content_object.author,
                    actor=self.request.user,
                    verb='回复',
                    description=description,
                    action_object=self.content_object)
        if self.request.is_ajax():
            data = {
                "status": "OK",
                "body": self.object.body,
                "html": render_to_string("sgscomment/_comment.html", {
                    "rec": self.object
                }, context_instance=RequestContext(self.request))
            }
            return JsonResponse(data)
        self.success_url = self.content_object.get_absolute_url()
        return super(CommentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            data = {
                "status": "ERROR",
                "errors": form.errors,
                "html": render_to_string("sgscomment/_comment.html", {
                    "form": form,
                    "obj": self.content_object
                }, context_instance=RequestContext(self.request))
            }
            return JsonResponse(data)
        return super(CommentCreateView, self).form_invalid(form)
