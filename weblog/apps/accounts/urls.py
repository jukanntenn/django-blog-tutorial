from django.conf.urls import url
from django.contrib.auth import views as auth_view

from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^login/$', auth_view.login, name='login', kwargs={'authentication_form': LoginForm}),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
