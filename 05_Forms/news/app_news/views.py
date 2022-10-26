from django.views.generic import ListView, DetailView, View, UpdateView
from app_news.models import News, Comment
from app_news.forms import CommentForm, NewsForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()


class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.id
        context['comment_list'] = Comment.objects.filter(news_id=self.object.id)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            news_comment = Comment.objects.create(**comment_form.cleaned_data)
            news_comment.news_id = pk
            news_comment.save()
            return HttpResponseRedirect(f'/news/{pk}')
        return render(request, 'news_detail.html', context={
            'comment_form': comment_form
        })


class NewsUpdateForm(UpdateView):
    model = News
    template_name = 'app_news/news_edit.html'
    fields = ['title', 'description']
    success_url = '/'


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():

            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news_list.html', context={'news_form': news_form})

