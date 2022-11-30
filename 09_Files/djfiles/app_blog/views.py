from _csv import reader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from app_blog.models import Post, Image
from app_blog.forms import PostForm, UploadPostsForm


class PostsListView(ListView):
    model = Post
    template_name = 'app_blog/posts_list.html'
    context_object_name = 'posts_list'
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'app_blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['images'] = Image.objects.filter(post=post)
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'app_blog/post_add.html'
    context_object_name = 'post_add'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        post = form.save()

        if form.is_valid():
            images = request.FILES.getlist('images')
            if images:
                for image in images:
                    instance = Image(image=image, post=post)
                    instance.save()
            post.user = request.user
            post.save()

        return HttpResponseRedirect('/')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'app_blog/post_edit.html'
    fields = ['description']
    success_url = '/'


def update_posts(request):
    if request.method == 'POST':
        upload_file_form = UploadPostsForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            posts_file = upload_file_form.cleaned_data['file'].read()
            posts_str = posts_file.decode('utf-8').split('\n')
            csv_reader = reader(posts_str, delimiter=';', quotechar='"')
            for row in csv_reader:
                print(row)
                Post.objects.create(description=row[0], created_at=row[1], user=request.user)
            return HttpResponse(content='Записи успешно добавлены', status=200)
    else:
        upload_file_form = UploadPostsForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'app_blog/upload_posts_file.html', context=context)
