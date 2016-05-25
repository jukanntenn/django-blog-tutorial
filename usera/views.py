from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect

from usera.forms import SignInForm, SignUpForm, ProfileForm, RestPasswordForm
from django.utils import timezone
from usera.models import ForumUser


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
        form.save()

        # Updating the password logs out all other sessions for the user
        # except the current one if
        # django.contrib.auth.middleware.SessionAuthenticationMiddleware
        # is enabled.
        update_session_auth_hash(self.request, form.user)
        return super(PassWordChangeView, self).form_valid(form)


class ProfileChangeView(UpdateView):
    form_class = ProfileForm
    template_name = 'usera/profile_change.html'
    model = ForumUser

    def form_valid(self, form):
        return super(ProfileChangeView, self).form_valid(form)


# class RestPasswordView(FormView):
#     form_class = RestPasswordForm
#     template_name = ''
#     success_url = '/blog'
#
#     def form_valid(self, form):
#         user = form.get_user()
#
#         new_password = uuid.uuid1().hex
#         user.set_password(new_password)
#         user.save()
#
#         # 给用户发送新密码
#         mail_title = u'django中国社区找回密码'
#         var = {'email': user.email, 'new_password': new_password}
#         mail_content = loader.get_template('user/forgot_password_mail.html').render(Context(var))
#         sendmail(mail_title, mail_content, user.email)
#
#         return ''


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/blog')
