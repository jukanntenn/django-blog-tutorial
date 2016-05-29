from django.forms import ModelForm, Textarea, CharField
from community.models import Post, Reply


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'topic']

        error_messages = {
            'title': {
                'max_length': "标题过长，最多70个字。"
            }
        }

        widgets = {
            'title': CharField(attrs={}),
            'body': Textarea(attrs={})
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

        widgets = {
            'content': Textarea(attrs={})
        }
