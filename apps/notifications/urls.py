from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notifications/$', views.AllNotificationsListView.as_view(), name='all_notifications'),
]
