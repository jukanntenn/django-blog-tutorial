from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

    def __init__(self, *args, **kwargs):
        # form 实例化是需要视图函数提供 user 参数
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.author = self.user
        post.save()
        return post
