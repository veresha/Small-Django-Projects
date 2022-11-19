from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=36, required=False)
    date_of_birth = forms.DateField(required=True, help_text='Дата регистрации')
    discount_card_num = forms.IntegerField(required=False, help_text='Номер дисконтной карты')
    tel_number = forms.IntegerField(required=False, help_text='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
