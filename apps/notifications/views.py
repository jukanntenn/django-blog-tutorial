from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Notifications


# Create your views here.
def mark_all_read(request):
    """将某个特定用户的全部通知全部标为已读，暂时重定向回首页
    TO-DO：修改重定向逻辑
    """
    notifications_set = Notifications.objects.filter(actor=request.user)
    notifications_set.update(unread=False)

    return HttpResponseRedirect('/')


def mark_as_read(request, notification_id):
    notifications = get_object_or_404(Notifications, pk=notification_id)
    notifications.mark_as_read()
    return HttpResponseRedirect('/')


class AllNotificationsListView(ListView):
    model = Notifications
    context_object_name = 'all_notification_list'
    template_name = 'notifications/notification_list.html'
