from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form

from account.models import User


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(Form):
    username = forms.CharField(max_length=50, min_length=6, error_messages={'min_length': '用户名长度至少6位'})
    password = forms.CharField(required=True, error_messages={'required': '必须填写密码'},
                               widget=forms.widgets.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise ValidationError('用户名不存在')
        return username
