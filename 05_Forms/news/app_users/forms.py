from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    city = forms.CharField(max_length=36, required=False, label='Город')
    tel_num = forms.IntegerField(required=False, label='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
