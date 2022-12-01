from django.contrib import admin
from app_blog.models import Post, Image


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'description', 'created_at']


@admin.register(Image)
class PostsImage(admin.ModelAdmin):
    list_display = ['image', 'post']

