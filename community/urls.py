from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^community/$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.PostDetailView.as_view(), name='detail'),
    # url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
]
