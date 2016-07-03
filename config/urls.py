from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('apps.blog.urls', namespace='blog', app_name='blog')),
    url(r'^usera/', include('apps.usera.urls', namespace='usera', app_name='usera')),
    url(r'', include('apps.commenta.urls', namespace='commenta', app_name='commenta')),
    url(r'', include('apps.community.urls', namespace='community', app_name='community')),
    url(r'', include('apps.notifications.urls', namespace='notifications', app_name='notifications')),
    url(r'', include('apps.likes.urls', namespace='likes', app_name='likes')),
    url(r'', include('apps.follow.urls', namespace='follow', app_name='follow')),
]
