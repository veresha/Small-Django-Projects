from django.contrib import admin
from app_news.models import News, Comment, Tag


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at', 'activity']
    list_filter = ['activity']
    inlines = [CommentInLine]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(activity=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(activity=False)

    mark_as_active.short_description = 'Перевести в статус "активно"'
    mark_as_inactive.short_description = 'Перевести в статус "неактивно"'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'comment_text', 'news']
    list_filter = ['user_name']
    actions = ['mark_as_deleted_by_admin']

    def mark_as_deleted_by_admin(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

    mark_as_deleted_by_admin.short_description = 'Перевести в статус "Удалено администратором"'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
