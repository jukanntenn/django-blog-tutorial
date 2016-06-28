from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Notifications
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def mark_all_read(request):
    """将某个特定用户的全部通知全部标为已读，暂时重定向回首页
    TO-DO：修改重定向逻辑
    """
    # genericforeignkey 获取对象有误，需修改正确方法
    request.user.notifications.mark_all_as_read()
    return HttpResponseRedirect('/')


def mark_as_read(request, notification_id):
    notifications = get_object_or_404(Notifications, pk=notification_id)
    notifications.mark_as_read()
    return HttpResponseRedirect('/')


class NotificationListMixin(object):
    model = Notifications
    context_object_name = 'all_notification_list'
    template_name = 'notifications/notification_list.html'

    def get_queryset(self):
        return self.request.user.notifications.all()


class AllNotificationsListView(NotificationListMixin, ListView):
    pass


class ReadNotificationsListView(NotificationListMixin, ListView):
    def get_queryset(self):
        return self.request.user.notifications.read()


class UnreadNotificationListView(NotificationListMixin, ListView):
    def get_queryset(self):
        return self.request.user.notifications.unread()


def mark_read(request, notification_id):
    # 暂时只返回首页
    notification = get_object_or_404(Notifications, pk=notification_id)
    notification.mark_as_read()
    return redirect('/')
