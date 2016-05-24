from django import forms
from django.forms import ModelForm
from usera.models import ForumUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.conf import settings


class SignInForm(ModelForm):

    class Meta:
        model = ForumUser
        fields = ['username', 'password']

    def clean(self, form=None):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise ValidationError('用户名或者密码不正确')
        return self.cleaned_data


class SignUpForm(ModelForm):

    class Meta:
        model = ForumUser
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            ForumUser.objects.get(username=username)
            raise forms.ValidationError('所填用户名已经被注册过')
        except ForumUser.DoesNotExist:
            if username in settings.RESERVED:
                raise forms.ValidationError('用户名被保留不可用')
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            ForumUser.objects.get(email=email)
            raise forms.ValidationError('所填邮箱已经被注册过')
        except ForumUser.DoesNotExist:
            return email

    def clean_password_confirm(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password_confirm']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('两次输入密码不一致')
        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
