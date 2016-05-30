from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^post/create/$', views.PostCreateView.as_view(), name='post_create')
]
