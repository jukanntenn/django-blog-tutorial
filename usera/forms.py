from django import forms
from django.forms import ModelForm
from pip.cmdoptions import help_
from usera.models import ForumUser, GENDER_CHOICES
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import re
from django.utils.translation import ugettext_lazy as _

class SignInForm(AuthenticationForm):
    error_messages = {
        'invalid_login': '用户名或密码错误',
        'inactive': '该账户已被冻结',
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if len(username) < 6 or len(username) > 18:
    #         raise forms.ValidationError('用户名长度6到18位')
    #
    #     if not re.match('^\w+$', username):
    #         raise forms.ValidationError('用户名应该只包含数字字母下划线')
    #     # 匹配数字字母下划线
    #     return username
    #    上面这样写好像有问题，先写在clean里面

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if len(username) < 6 or len(username) > 18:
            raise forms.ValidationError('用户名长度6到18位')

        if not re.match('^\w+$', username):
            raise forms.ValidationError('用户名应该只包含数字字母下划线')
        # 匹配数字字母下划线
        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


# class SignInForm(ModelForm):
#     class Meta:
#         model = ForumUser
#         fields = ['username', 'password']
#
#     def clean(self, form=None):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#
#         if username and password:
#             user_cache = authenticate(username=username, password=password)
#             if user_cache is None:
#                 raise ValidationError('用户名或者密码不正确')
#         return self.cleaned_data


# class SignUpForm(ModelForm):
#     class Meta:
#         model = ForumUser
#         fields = ['username', 'email', 'password']
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             ForumUser.objects.get(username=username)
#             raise forms.ValidationError('所填用户名已经被注册过')
#         except ForumUser.DoesNotExist:
#             if username in settings.RESERVED:
#                 raise forms.ValidationError('用户名被保留不可用')
#             return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             ForumUser.objects.get(email=email)
#             raise forms.ValidationError('所填邮箱已经被注册过')
#         except ForumUser.DoesNotExist:
#             return email
#
#     def clean_password_confirm(self):
#         password1 = self.cleaned_data['password']
#         password2 = self.cleaned_data['password_confirm']
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('两次输入密码不一致')
#         return password2
#
#     def save(self, commit=True):
#         user = super(SignUpForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user

class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "两次输入的密码不匹配",
    }

    class Meta:
        model = ForumUser
        fields = ("username", 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = '用户名长度6位到30位'
        self.fields['password1'].help_text = '密码长度6位到32位'
        self.fields['password2'].help_text = '请重复输入密码'

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match('^\w+$', username):
            raise forms.ValidationError('用户名应该只包含数字字母下划线')
        # 匹配数字字母下划线
        if len(username) < 6 or len(username) > 18:
            raise forms.ValidationError('用户名长度6到18位')

        try:
            ForumUser.objects.get(username=username)
            raise forms.ValidationError('该用户名已被注册', code='registered')
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

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class ProfileForm(forms.Form):
#     mugshot = forms.ImageField(label=u'头像', required=True, error_messages={'invalid': u'头像格式要求？'})
#     gender = forms.ChoiceField(label=u'性别', required=True, choices=GENDER_CHOICES)
#     birthday = forms.DateField(label=u'生日', required=True)
#     self_intro = forms.Textarea()
#     website = forms.URLField(label=u'个人网站', required=True, max_length=200, min_length=10, error_messages={
#         'invalid': u'输入个人网站',
#         'max_length': u'不能超过200个字符',
#         'min_length': u'不能少于10个字符'
#     })
#     github = forms.URLField(label=u'GitHub主页', required=True, max_length=200, min_length=10, error_messages={
#         'invalid': u'输入GitHub主页',
#         'max_length': u'不能超过200个字符',
#         'min_length': u'不能少于10个字符'
#     })
#     nickname = forms.CharField(label=u'昵称', required=True, max_length=20, min_length=2, error_messages={
#         'invalid': u'输入昵称',
#         'max_length': u'不能超过20个字符',
#         'min_length': u'不能少于2个字符'
#     })
#     sector = forms.CharField(label=u'所在单位', required=True, max_length=20, min_length=2, error_messages={
#         'invalid': u'输入所在单位',
#         'max_length': u'不能超过20个字符',
#         'min_length': u'不能少于2个字符'
#     })
#     position = forms.CharField(label=u'职位', required=True, max_length=20, min_length=2, error_messages={
#         'invalid': u'输入职位',
#         'max_length': u'不能超过20个字符',
#         'min_length': u'不能少于2个字符'
#     })
#     last_login_ip = forms.GenericIPAddressField(label='最后一次登录IP', required=False)
#
#     def get_id(self):
#         return self.cleaned_data['usera_id']
#
#     def clean_profile_id(self):
#         if self.get_id():
#             try:
#                 ForumUser.objects.get(id=self.get_id())
#             except ForumUser.DoesNotExist:
#                 raise forms.ValidationError(u'提交数据有误')
#         return self.get_id()
#
#     def clean_nickname(self):
#         if self.get_id():
#             try:
#                 usera = ForumUser.objects.get(id=self.get_id())
#                 try:
#                     onickname = usera.nickname
#                     ForumUser.objects.exclude(nickname=onickname).get(nickname=self.cleaned_data['nickname'])
#                     raise forms.ValidationError(u'昵称已经存在')
#                 except ForumUser.DoesNotExist:
#                     return self.cleaned_data['nickname']
#             except ForumUser.DoesNotExist:
#                 raise forms.ValidationError(u'数据非法')
#         return self.cleaned_data['nickname']
#
#         # Other method ?
#         onickname = self.cleaned_data['nickname']
#         try:
#             ForumUser.objects.get(nickname__exact=onickname)
#         except ForumUser.DoesNotExist:  # Maybe throw error MultipleObjectsReturned: get() returned more than one
#             return self.cleaned_data['nickname']
#
#     def update(self):
#         user = ForumUser.objects.get(id=self.get_id())
#         user.mugshot = self.cleaned_data['mugshot']
#         user.gender = self.cleaned_data['gender']
#         user.birthday = self.cleaned_data['birthday']
#         user.self_intro = self.cleaned_data['self_intro']
#         user.website = self.cleaned_data['website']
#         user.github = self.cleaned_data['github']
#         user.nickname = self.cleaned_data['nickname']
#         user.sector = self.cleaned_data['sector']
#         user.position = self.cleaned_data['position']
#         user.last_login_ip = self.cleaned_data['last_login_ip']
#         user.save()
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ForumUser
        fields = ('nickname', 'mugshot', 'gender', 'birthday', 'self_intro',
                  'website', 'github',  'sector', 'position')

        help_texts = {
            'mugshot': '上传jpg/png格式图片',
            'self_intro': '%d/%d' % (5, 120)
        }
        error_messages = {
            'mugshot':{
                'invalid': '上传jpg/png格式图片',
            },
            'nickname':{
                'invalid': u'输入您的昵称',
                'max_length': u'不能超过12个字符',
                'min_length': u'不能少于2个字符'
            },
            'self_intro': {
                'invalid': u'您的说明',
                'max_length': u'不能超过120个字符',
                'min_length': u'不能少于20个字符'
            },
        }
    def clean_nickname(self):
        onickname = self.cleaned_data['nickname']
        try:
            ForumUser.objects.get(nickname__exact=onickname)
            raise forms.ValidationError(u'昵称已存在')
        except ForumUser.DoesNotExist:
            return onickname

    def clean_mugshot(self):
        pass
        omugshot = self.cleaned_data['mugshot']
        if not str(omugshot.name).endswith('.jpg') or not str(omugshot.name).endswith('.png'):
            raise forms.ValidationError(u'请上传jpg/png格式图像', code='FormatError')
        else:
            return omugshot

    def save(self, commit=True):
        try:
            #self.full_clean(exclude=('last_login_ip', 'username', 'password1', 'password2'))
            self.full_clean(exclude=not self.fields)
        except ValidationError as e:
            raise e.message_dict[NON_FIELD_ERRORS]
        profile = super(ProfileForm, self).save(commit=commit)



class RestPasswordForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(RestPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username').strip().lower()
        email = self.cleaned_data.get('email')
        if username and email:
            try:
                self.user_cache = ForumUser.objects.get(username=username, email=email)
            except ForumUser.DoesNotExist:
                raise forms.ValidationError('所填用户名或邮箱错误')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


