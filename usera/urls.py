from django.conf.urls import url
from usera import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signin/$', views.SignInView.as_view(), name='signin'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^password_change/$', views.PassWordChangeView.as_view(), name='password_change'),
]
