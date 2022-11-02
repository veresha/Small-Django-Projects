from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from app_users.forms import RegisterForm
from app_users.models import Profile


class UsersLoginView(LoginView):
    template_name = 'users/login.html'


class UsersLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def profile_view(request):
    return render(request, 'users/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            tel_num = form.cleaned_data.get('tel_num')
            news_amount = form.cleaned_data.get('news_amount')
            verification = form.cleaned_data.get('verification')
            Profile.objects.create(
                user=user,
                city=city,
                tel_num=tel_num,
                news_amount=news_amount,
                verification=verification,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

