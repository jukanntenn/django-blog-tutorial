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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.obj = kwargs.pop('obj')
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.author = self.user
        post.save()
        return post


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

        widgets = {
            'content': Textarea(attrs={})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.user = kwargs.pop('user')
        super(ReplyForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        reply = super(ReplyForm, self).save(commit=False)
        reply.reply_user = self.user
        reply.save()
        return reply
