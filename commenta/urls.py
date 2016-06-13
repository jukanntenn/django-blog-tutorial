from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', views.SgsCommentCreateView.as_view(),
        name='post_comment'),
    url(r'^comment/(?P<content_type_id>\d+)/(?P<object_id>\d+)/(?P<parent_id>\d+)/$',
        views.SgsCommentCreateView.as_view(),
        name='post_child_comment'),
]
