from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from app_users.forms import RegisterForm
from django.views.generic import UpdateView


class UserUpdateView(UpdateView):
    model = User
    template_name = 'app_users/profile_edit.html'
    fields = ['username', 'first_name', 'last_name']
    success_url = '/users/profile'


class UsersLoginView(LoginView):
    template_name = 'app_users/login.html'


class UsersLogoutView(LogoutView):
    next_page = '/'


def profile_view(request):
    return render(request, 'app_users/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = user.cleaned_data.get('username')
            raw_password = user.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})

