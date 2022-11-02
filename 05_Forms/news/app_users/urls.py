from django.urls import path
from app_users.views import UsersLoginView, UsersLogoutView, register_view, profile_view


urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile')

]
