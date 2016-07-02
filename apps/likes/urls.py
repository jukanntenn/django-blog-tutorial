from django.conf.urls import include, url
from . import views

# http://localhost:8000/likes/ +
# 在project的urls.py导入整个url配置
urlpatterns = [
    url(r"^like/(?P<content_type_id>\d+):(?P<object_id>\d+)/$",
        views.LikeToggleView.as_view(),
        name="like_toggle"),
]
