from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets

from registration.forms import RegistrationFormUniqueEmail


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "用户名"})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': "密码"})


class RegisterForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "用户名"})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': "邮箱"})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder': "密码"})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder': "确认密码"})
