from django.contrib import admin
from advertisements_app.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

