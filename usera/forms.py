from django import forms
from django.forms import ModelForm
from usera.models import ForumUser, GENDER_CHOICES
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
            user_cache = authenticate(username=username, password=password)
            if user_cache is None:
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


class ProfileForm(forms.Form):
    mugshot = forms.ImageField(label=u'头像', required=True, error_messages={'invalid': u'头像格式要求？'})
    gender = forms.ChoiceField(label=u'性别', required=True, choices=GENDER_CHOICES)
    birthday = forms.DateField(label=u'生日', required=True)
    self_intro = forms.Textarea()
    website = forms.URLField(label=u'个人网站', required=True, max_length=200, min_length=10, error_messages={
        'invalid': u'输入个人网站',
        'max_length': u'不能超过200个字符',
        'min_length': u'不能少于10个字符'
    })
    github = forms.URLField(label=u'GitHub主页', required=True, max_length=200, min_length=10, error_messages={
        'invalid': u'输入GitHub主页',
        'max_length': u'不能超过200个字符',
        'min_length': u'不能少于10个字符'
    })
    nickname = forms.CharField(label=u'昵称', required=True, max_length=20, min_length=2, error_messages={
        'invalid': u'输入昵称',
        'max_length': u'不能超过20个字符',
        'min_length': u'不能少于2个字符'
    })
    sector = forms.CharField(label=u'所在单位', required=True, max_length=20, min_length=2, error_messages={
        'invalid': u'输入所在单位',
        'max_length': u'不能超过20个字符',
        'min_length': u'不能少于2个字符'
    })
    position = forms.CharField(label=u'职位', required=True, max_length=20, min_length=2, error_messages={
        'invalid': u'输入职位',
        'max_length': u'不能超过20个字符',
        'min_length': u'不能少于2个字符'
    })
    last_login_ip = forms.GenericIPAddressField(label='最后一次登录IP', required=False)

    def get_id(self):
        return self.cleaned_data['usera_id']

    def clean_profile_id(self):
        if self.get_id():
            try:
                ForumUser.objects.get(id=self.get_id())
            except ForumUser.DoesNotExist:
                raise forms.ValidationError(u'提交数据有误')
        return self.get_id()

    def clean_nickname(self):
        if self.get_id():
            try:
                usera = ForumUser.objects.get(id=self.get_id())
                try:
                    onickname = usera.nickname
                    ForumUser.objects.exclude(nickname=onickname).get(nickname=self.cleaned_data['nickname'])
                    raise forms.ValidationError(u'昵称已经存在')
                except ForumUser.DoesNotExist:
                    return self.cleaned_data['nickname']
            except ForumUser.DoesNotExist:
                raise forms.ValidationError(u'数据非法')
        return self.cleaned_data['nickname']

        # Other method ?
        onickname = self.cleaned_data['nickname']
        try:
            ForumUser.objects.get(nickname__exact=onickname)
        except ForumUser.DoesNotExist:  # Maybe throw error MultipleObjectsReturned: get() returned more than one
            return self.cleaned_data['nickname']

    def update(self):
        user = ForumUser.objects.get(id=self.get_id())
        user.mugshot = self.cleaned_data['mugshot']
        user.gender = self.cleaned_data['gender']
        user.birthday = self.cleaned_data['birthday']
        user.self_intro = self.cleaned_data['self_intro']
        user.website = self.cleaned_data['website']
        user.github = self.cleaned_data['github']
        user.nickname = self.cleaned_data['nickname']
        user.sector = self.cleaned_data['sector']
        user.position = self.cleaned_data['position']
        user.last_login_ip = self.cleaned_data['last_login_ip']
        user.save()
