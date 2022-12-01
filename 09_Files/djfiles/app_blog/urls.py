from .views import PostsListView, PostDetailView, PostCreateView, PostUpdateView, update_posts
from django.urls import path


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('update_posts/', update_posts, name='update-posts'),
]
