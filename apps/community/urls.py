from django.conf.urls import url

from apps.community import views

urlpatterns = [
    url(r'^create-post/$', views.PostCreateView.as_view(), name='create_post'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.PostDetailView.as_view(), name='detail'),
]
