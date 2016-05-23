from django.conf.urls import url
from usera import views

urlpatterns = [
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]
