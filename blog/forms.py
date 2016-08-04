from django import forms
from .models import Article, ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['body']
