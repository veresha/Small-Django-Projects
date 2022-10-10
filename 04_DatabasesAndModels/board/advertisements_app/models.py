from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Название')
    description = models.TextField(max_length=1500, default='', verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey('AuthorContactInfo', default=None, null=True, on_delete=models.CASCADE,
                               related_name='author', verbose_name='Автор')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, on_delete=models.CASCADE,
                                 related_name='category', verbose_name='Категория')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='type', verbose_name='Тип объявления')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AuthorContactInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Адрес электронной почты')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ['name']


class AdvertisementCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'
        ordering = ['category_name']


class AdvertisementType(models.Model):
    advertisement_type = models.CharField(max_length=50, verbose_name='Тип объявления')

    def __str__(self):
        return self.advertisement_type

    class Meta:
        db_table = 'type'
        ordering = ['advertisement_type']
