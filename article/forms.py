from django import forms
from django.core.exceptions import ValidationError

from article.models import Article

MAX_BLOG_LENGTH = 140


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['content','user']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_BLOG_LENGTH:
            raise forms.ValidationError("长度不能超过140个字")
        return content
