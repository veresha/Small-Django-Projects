from django import forms
from app_news.models import Comment, News


class NewsForm(forms.Form):
    title = forms.CharField(label='Заголовок')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 3}), label='Описание')


class CommentForm(forms.Form):
    user_name = forms.CharField(label='Имя пользователя')
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 3}), label='Комментарий')


class AuthCommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 3}), label='Комментарий')
