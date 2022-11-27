from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Изображения', required=False)

    class Meta:
        model = Post
        fields = ['description']


class UploadPostsForm(forms.Form):
    file = forms.FileField(label='Файл')
