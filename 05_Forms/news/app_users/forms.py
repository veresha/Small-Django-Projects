from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=36, required=False, help_text='Город')
    tel_num = forms.IntegerField(required=False, help_text='Номер телефона')
    # news_amount = forms.IntegerField(required=False, help_text='Количество опубликованных новостей')
    # verification = forms.BooleanField(required=False, help_text='Верификация')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
