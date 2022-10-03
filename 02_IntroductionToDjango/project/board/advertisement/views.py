from django.shortcuts import render
from django.http import HttpResponse


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
