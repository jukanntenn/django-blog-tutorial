from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from .forms import SgsCommentForm
from .models import SgsComment


# Create your views here.

class SgsCommentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = SgsCommentForm
    model = SgsComment
    content_object = None
    parent_comment = None
    object = None
    template_name = 'records/detail.html'

    def get_form_kwargs(self):
        kwargs = super(SgsCommentCreateView, self).get_form_kwargs()
        kwargs.update({
            "request": self.request,
            "obj": self.content_object,
            "user": self.request.user,
            "parent": self.parent_comment,
        })
        return kwargs

    def post(self, request, *args, **kwargs):
        content_type = get_object_or_404(ContentType, pk=self.kwargs.get("content_type_id"))
        self.content_object = content_type.get_object_for_this_type(pk=self.kwargs.get("object_id"))
        try:
            self.parent_comment = SgsComment.objects.get(id=self.kwargs.get("parent_id"))
        except SgsComment.DoesNotExist:
            self.parent_comment = None
        return super(SgsCommentCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
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
        return super(SgsCommentCreateView, self).form_valid(form)

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
        context = {
            'rec': self.content_object,
            'form': form
        }
        return render(self.request, self.template_name, context=context)
