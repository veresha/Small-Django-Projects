from django.urls import path
from .views import NewsListView, NewsDetailView, NewsFormView, NewsUpdateForm


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/edit/', NewsUpdateForm.as_view(), name='news-edit'),
    path('news_add/', NewsFormView.as_view(), name='news-add'),
]
