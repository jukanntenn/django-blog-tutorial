from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import SgsComment


class SgsCommentForm(forms.ModelForm):
    class Meta:
        model = SgsComment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.obj = kwargs.pop("obj")
        self.user = kwargs.pop("user")
        self.parent = kwargs.pop("parent", None)
        super(SgsCommentForm, self).__init__(*args, **kwargs)

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise forms.ValidationError('说点什么吧？')
        return body

    def save(self, commit=True):
        comment = super(SgsCommentForm, self).save(commit=False)
        comment.content_type = ContentType.objects.get_for_model(self.obj)
        comment.object_id = self.obj.pk
        comment.author = self.user
        if self.parent:
            comment.parent = self.parent
        if commit:
            comment.save()
        return comment
