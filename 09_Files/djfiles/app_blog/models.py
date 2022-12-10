from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='Пользователи', default='1')
    description = models.CharField(max_length=200, verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']
        verbose_name_plural = _('posts')
        verbose_name = _('post')


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, verbose_name=_('post'))

    class Meta:
        verbose_name_plural = _('images')
        verbose_name = _('image')
