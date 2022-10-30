from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView


class UsersLoginView(LoginView):
    template_name = 'users/login.html'


class UsersLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'

