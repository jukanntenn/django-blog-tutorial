from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponseRedirect
from django.views.generic.base import View
from apps.commenta.views import CommentLoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from .models import Like


class LikeToggleView(CommentLoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        content_type = get_object_or_404(ContentType, pk=self.kwargs.get("content_type_id"))
        try:
            obj = content_type.get_object_for_this_type(pk=self.kwargs.get("object_id"))
        except ObjectDoesNotExist:
            raise Http404("Object not found.")
        Like.objects.like_toggle(request.user, content_type, obj.id)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
