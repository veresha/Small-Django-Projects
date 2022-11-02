from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True, verbose_name='город')
    tel_num = models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')
    news_amount = models.IntegerField(default=0, null=True, blank=True, verbose_name='Количество новостей')
    verification = models.BooleanField(default=False, null=True, blank=True, verbose_name='Верификация')

    class Meta:
        permissions = (
            ('can_verify', 'Может верифицировать'),
        )
