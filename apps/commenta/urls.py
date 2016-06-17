from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^comment/$', views.CommentCreateView.as_view(), name='post_comment'),
]
