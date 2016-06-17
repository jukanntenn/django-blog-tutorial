from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import Comment


class CommentForm(forms.ModelForm):
    content_type_id = forms.CharField(widget=forms.HiddenInput)
    object_pk = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, target_object, initial=None, **kwargs):
        self.target_object = target_object
        self.request = kwargs.pop("request", None)
        self.obj = target_object
        self.user = kwargs.pop("user")
        self.parent = kwargs.pop("parent", None)
        if initial is None:
            initial = {}
            initial.update({
                'content_type_id': ContentType.objects.get_for_model(self.target_object).pk,
                'object_pk': self.target_object.pk,
            })
        super(CommentForm, self).__init__(initial=initial, **kwargs)

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise forms.ValidationError('说点什么吧？')
        return body

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.content_type = ContentType.objects.get_for_model(self.obj)
        comment.object_id = self.obj.pk
        comment.author = self.user
        if self.parent:
            comment.parent = self.parent
        if commit:
            comment.save()
        return comment
