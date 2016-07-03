from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r"^follow/(?P<content_type_id>\d+):(?P<object_id>\d+)/$",
        views.FollowToggleView.as_view(),
        name="follow_toggle"),
]
