from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import FormView

from usera.forms import SignInForm, SignUpForm
from django.utils import timezone


class SignInView(FormView):
    template_name = 'usera/signin.html'
    form_class = SignInForm
    success_url = '/blog'

    def form_valid(self, form):
        user = form.get_user()
        # 用户登录时，需要更新他的last_login_time，last_login_ip
        if user.is_active:
            login(self.request, user)
            user.last_login_time = timezone.now()
            user.last_login_ip = self.request.META.get("REMOTE_ADDR", None)
            user.save(update_fields=['last_login_time', 'last_login_ip'])
        else:
            pass
        return super(SignInView, self).form_valid(form)


class SignUpView(FormView):
    template_name = 'usera/signup.html'
    form_class = SignUpForm
    success_url = '/blog'

    def form_valid(self, form):
        # 用户注册时，为其设置一个默认头像和设置其注册的IP
        user = form.save(commit=False)
        user.sign_up_ip = self.request.META.get("REMOTE_ADDR", None)
        user.last_login_ip = self.request.META.get("REMOTE_ADDR", None)
        user.last_login_time = timezone.now()
        user.save()
        return super(SignUpView, self).form_valid(form)


class PassWordChangeView(FormView):
    template_name = 'usera/password_change.html'
    form_class = PasswordChangeForm
    success_url = '/blog'

    def get_form_kwargs(self):
        kwargs = super(PassWordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        return super(PassWordChangeView, self).form_valid(form)
