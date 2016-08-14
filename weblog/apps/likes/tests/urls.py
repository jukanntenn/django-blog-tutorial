from django.conf.urls import include, url
from django.http import HttpResponse


def dummy_view():
    return HttpResponse(content=b'', status=200)

urlpatterns = [
    url(r"^", include("pinax.likes.urls", namespace="pinax_likes")),
    url(r"^dummy_login/$", dummy_view, name="account_login"),
]
