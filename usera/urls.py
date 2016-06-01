from django.conf.urls import url
from usera import views

urlpatterns = [
    url(r'^sign-in/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^sign-up/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^password-change/$', views.PassWordChangeView.as_view(), name='password_change'),
    url(r'^password-reset/$', views.ResetPasswordView.as_view(), name='password_reset'),
    # url(r'^profile_change/(?P<pk>[0-9]+)/$', views.ProfileChangeView.as_view(), name='profile_change'),
    url(r'^log-out/$', views.log_out, name='log_out'),
]
