from django.contrib import admin
from advertisements_app.models import Advertisement, AuthorContactInfo, AdvertisementCategory


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']


@admin.register(AuthorContactInfo)
class AuthorContactInfoAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


# admin.site.register(Advertisement, AdvertisementAdmin)
