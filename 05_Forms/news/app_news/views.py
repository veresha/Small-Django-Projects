from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, View, UpdateView
from app_news.models import News, Comment, Tag
from app_users.models import Profile
from app_news.forms import CommentForm, NewsForm, AuthCommentForm, PublishForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        queryset = super(NewsListView, self).get_queryset()
        tag = self.request.GET
        print(tag)
        if tag:
            queryset.filter(tag)
        return queryset


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
        if request.user.has_perm('app_users.can_publish'):
            news = News.objects.get(id=pk)
            news.activity = True
            news.save()
            return HttpResponseRedirect(f'/news/{pk}')
        if request.user.is_authenticated:
            comment_form = AuthCommentForm(request.POST)
        else:
            comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_post = Comment.objects.create(**comment_form.cleaned_data)

            if request.user.is_authenticated:
                comment_post.user_name = request.user.username
                comment_post.user = request.user
            else:
                comment_post.user_name = comment_form['user_name'].value() + " (аноним)"
            comment_post.news_id = pk
            comment_post.save()
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
        if not request.user.profile.verification:
            raise PermissionDenied()
        news_form = NewsForm()
        return render(request, 'app_news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            user = Profile.objects.get(id=request.user.id)
            user.news_amount += 1
            user.save()
            return HttpResponseRedirect('/')
        return render(request, 'news_list.html', context={'news_form': news_form})
