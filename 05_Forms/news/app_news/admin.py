from django.contrib import admin
from app_news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'comment_text', 'news', 'pk']
