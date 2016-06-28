from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Notifications


# Create your views here.
def mark_all_read(request):
    """将某个特定用户的全部通知全部标为已读，暂时重定向回首页
    TO-DO：修改重定向逻辑
    """
    # genericforeignkey 获取对象有误，需修改正确方法
    notifications_set = Notifications.objects.filter(actor=request.user)
    notifications_set.update(unread=False)

    return HttpResponseRedirect('/')


def mark_as_read(request, notification_id):
    notifications = get_object_or_404(Notifications, pk=notification_id)
    notifications.mark_as_read()
    return HttpResponseRedirect('/')


class NotificationListMixin(object):
    model = Notifications
    context_object_name = 'all_notification_list'
    template_name = 'notifications/notification_list.html'


class AllNotificationsListView(NotificationListMixin, ListView):
    pass


class ReadNotificationsListView(NotificationListMixin, ListView):
    queryset = Notifications.objects.read()


class UnreadNotificationListView(NotificationListMixin, ListView):
    queryset = Notifications.objects.unread()


def mark_read(request, notification_id):
    # 暂时只返回首页
    notification = get_object_or_404(Notifications, pk=notification_id)
    notification.mark_as_read()
    return redirect('/')
