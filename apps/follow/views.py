from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
# 关注某个帖子
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from django.views.generic.edit import CreateView

from apps.notifications.signals import notify
from .models import Follow

def follow_change(self, request):

    '''
    handle follow state
    @param {ctype_pk} content type id
    @param {object_pk} Object pk
    @param {state} follow or unfollow
    '''
    ctype_pk = self.request.GET.get('content_type_id')
    object_pk = self.request.GET.get('object_pk')
    state = True if request.GET.get('state') == True else False

    content_type = get_object_or_404(ContentType, pk = int(ctype_pk))
    self.content_object = content_type.get_object_for_this_type(pk = int(object_pk))
        
    # get followers
    try:
        followers = Follow.objects.get(content_type = content_type, object_pk = object_pk)
    except Exception:
        # no followers, then create one
        followers = Follow(content_type = content_type, object_pk = object_pk)
