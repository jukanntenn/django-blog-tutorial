from django import forms
from .models import Article, ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['user_name', 'user_email', 'body']
