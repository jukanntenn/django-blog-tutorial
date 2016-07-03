import string
import random
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import HttpResponseRedirect
from django.utils import timezone

from apps.usera.models import CommunityUser
from .forms import SignInForm, SignUpForm, ResetPasswordForm
#from itsdangerous import URLSafeSerializer as utsr
#from config.settings import SECRET_KEY as security_key
import base64

#security_key = 'DjangoBlog'

class SignInView(FormView):
    template_name = 'usera/signin.html'
    form_class = SignInForm

    # success_url = '/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        # 用户登录时，需要更新他的last_login_time，last_login_ip
        if user.is_active:
            form.save(self.request, user)
        return super(SignInView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignInView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        redirect_to = self.request.POST['next']
        # from next we got string 'None',not None
        if redirect_to != 'None':
            return redirect_to
        return '/'

# 更安全的加密方法，还没完全弄懂
# create token used in activate link
# class Token(object):
#     def __init__(self, security_key):
#         self.security_key = security_key
#         self.salt = base64.encodestring(security_key)
#
#     def generate_validate_token(self, username):
#         serializer = utsr(self.security_key)
#         return serializer.dump(username, self.salt)
#
#     def confirm_validate_token(self, token, expiration=3600):
#         serializer = utsr(self.security_key)
#         return serializer.loads(token, salt=self.salt, max_age=expiration)
#
# token_confirm = Token


def generate_token(username):
    token = base64.b64encode(username.encode('ascii'))
    return token


def confirm_token(token):
    username = base64.b64decode(token)
    return username


# send  activate mail
def active_mail(username, email):
    token = generate_token(username)
    host = 'smtp.163.com'  # 设置发件服务器地址
    port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
    sender = 'upczww@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
    pwd = '15763928103z'  # 设置发件邮箱的密码，等会登陆会用到
    receiver = email  # 设置邮件接收人
    body = '<h1>Django中国社区用户激活</h1><p>请点击以下链接激活用户</p>'+'http://127.0.0.1:8000/usera/activate/'+token.decode(encoding='UTF-8')# 设置邮件正文，这里是支持HTML的

    msg = MIMEText(body, 'html')  # 设置正文为符合邮件格式的HTML内容
    msg['subject'] = 'Django中国社区密码重置'  # 设置邮件标题
    msg['from'] = sender  # 设置发送人
    msg['to'] = receiver  # 设置接收人
    try:
        s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)  # 登陆邮箱
        s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！
    except smtplib.SMTPException:
        pass


# use email to active user
def active_user(request, token):
    username = confirm_token(token)
    try:
        user = CommunityUser.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')
    user.is_active = True
    user.save()
    return HttpResponse(u'用户已经激活')


class SignUpView(FormView):
    template_name = 'usera/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.sign_up_ip = self.request.META.get("REMOTE_ADDR", None)
        user.date_joined = timezone.now()
        user.is_active = False
        active_mail(form.clean_username(), email=form.clean_email())
        user.save()
        return super(SignUpView, self).form_valid(form)


class PassWordChangeView(FormView):
    template_name = 'usera/password_change.html'
    form_class = PasswordChangeForm
    success_url = '/'

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


# class ProfileChangeView(UpdateView):
#     form_class = ProfileForm
#     template_name = 'usera/profile_change.html'
#     model = ForumUser
#
#     def form_valid(self, form):
#         return super(ProfileChangeView, self).form_valid(form)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'usera/password_reset.html'
    success_url = '/'

    def randomstr(self, length=20):
        letters = list(string.ascii_letters + string.digits)
        randstring = ""
        for i in range(length):
            randstring += random.choice(letters)
        return randstring

    def form_valid(self, form):
        user = form.get_user()
        new_password = self.randomstr()
        user.set_password(new_password)
        user.save()

        host = 'smtp.163.com'  # 设置发件服务器地址
        port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
        sender = 'upczww@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
        pwd = 'password'  # 设置发件邮箱的密码，等会登陆会用到
        receiver = user.email  # 设置邮件接收人
        body = '<h1>Django中国社区密码重置</h1><p>您的新密码为：' + new_password + '</p>'  # 设置邮件正文，这里是支持HTML的

        msg = MIMEText(body, 'html')  # 设置正文为符合邮件格式的HTML内容
        msg['subject'] = 'Django中国社区密码重置'  # 设置邮件标题
        msg['from'] = sender  # 设置发送人
        msg['to'] = receiver  # 设置接收人
        try:
            s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s.login(sender, pwd)  # 登陆邮箱
            s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！
        except smtplib.SMTPException:
            pass
        return super(ResetPasswordView, self).form_valid(form)
