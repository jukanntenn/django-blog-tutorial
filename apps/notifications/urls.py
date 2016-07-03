from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notifications/$', views.AllNotificationsListView.as_view(), name='all_notifications'),
    url(r'^notifications/read/$', views.ReadNotificationsListView.as_view(), name='read_notifications'),
    url(r'^notifications/unread/$', views.UnreadNotificationListView.as_view(), name='unread_notifications'),
    url(r'^notifications/mark-read/(?P<notification_id>\d+)/$', views.mark_read, name='mark_read'),
    url(r'^notifications/mark-all-read/$', views.mark_all_read, name='mark_all_read'),
]
