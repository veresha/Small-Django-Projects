from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1500, default='', verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True)
    activity = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        ordering = ['created_at']
        permissions = (
            ('can_publish', 'Может публиковать'),
        )


class Comment(models.Model):
    user_name = models.CharField(max_length=100, default='', verbose_name='Имя пользователя')
    comment_text = models.TextField(max_length=1500, default='', verbose_name='Текст комментария')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name='news', verbose_name='Новость')
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        db_table = 'comments'
