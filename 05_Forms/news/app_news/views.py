from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, View, UpdateView
from app_news.models import News, Comment
from app_news.forms import CommentForm, NewsForm, AuthCommentForm
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

    # @permission_required('app_news.view_news_add')
    def get(self, request):
        # if not request.user.has_perm('app_news.add_news_add'):
        if not request.user.profile.verification:
            raise PermissionDenied()
        news_form = NewsForm()
        return render(request, 'app_news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():

            News.objects.create(**news_form.cleaned_data)
            # request.user.news_count += 1
            return HttpResponseRedirect('/')
        return render(request, 'news_list.html', context={'news_form': news_form})
