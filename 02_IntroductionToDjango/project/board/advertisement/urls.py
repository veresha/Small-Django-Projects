from django.urls import path
from .import views

urlpatterns = [
    path('regions/', views.Regions.as_view()),
    path("", views.advertisement_list, name='advertisement_list'),
    path('advertisement/', views.advertisement_detail, name='advertisement_list'),
    path('python_basic/', views.advertisement_python_basic, name='python_basic'),
    path('git/', views.advertisement_git, name='git'),
    path('html/', views.advertisement_html, name='html'),
    path('sql/', views.advertisement_sql, name='sql'),
    path('english/', views.advertisement_english, name='english'),
]
