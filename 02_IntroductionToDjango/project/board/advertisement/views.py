from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


class Regions(TemplateView):
    template_name = 'advertisement/regions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        return context

    def post(self, request):
        mes = 'регион успешно создан'
        return render(request, 'advertisement/regions.html', {'mes': mes})


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_detail(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/python_basic.html', {})


def advertisement_git(request, *args, **kwargs):
    return render(request, 'advertisement/git.html', {})


def advertisement_html(request, *args, **kwargs):
    return render(request, 'advertisement/html.html', {})


def advertisement_sql(request, *args, **kwargs):
    return render(request, 'advertisement/sql.html', {})


def advertisement_english(request, *args, **kwargs):
    return render(request, 'advertisement/english.html', {})
