"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'', include('comments.urls')),
    url(r'', include('django_comments.urls')),
    url(r'', include('accounts.urls')),
    url(r'', include('registration.backends.default.urls')),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^search/', include('haystack.urls')),
    url('^notifications/', include('notifications.urls', namespace='notifications')),
    url(r'^likes/', include('likes.urls', namespace='pinax_likes')),
    url(r'', include('social_login.urls', namespace='social_login')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
