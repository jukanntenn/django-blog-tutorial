from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import (
    Http404,
    HttpResponseForbidden,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import View

from .models import Like
from .signals import object_liked, object_unliked
from .utils import widget_context

from .compat import LoginRequiredMixin


class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        content_type = get_object_or_404(ContentType, pk=self.kwargs.get("content_type_id"))
        try:
            obj = content_type.get_object_for_this_type(pk=self.kwargs.get("object_id"))
        except ObjectDoesNotExist:
            raise Http404("Object not found.")

        if not request.user.has_perm("likes.can_like", obj):
            return HttpResponseForbidden()

        like, liked = Like.like(request.user, content_type, obj.id)

        if liked:
            object_liked.send(sender=Like, like=like, request=request)
        else:
            object_unliked.send(sender=Like, object=obj, request=request)

        if request.is_ajax():
            html_ctx = widget_context(request.user, obj)
            template = "pinax/likes/_widget.html"
            if request.GET.get("t") == "b":
                template = "pinax/likes/_widget_brief.html"
            data = {
                "html": render_to_string(
                        template,
                        context=html_ctx,
                        request=request
                ),
                "likes_count": html_ctx["like_count"],
                "liked": html_ctx["liked"],
            }
            return JsonResponse(data)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
