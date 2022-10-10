from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from advertisements.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements/advertisements.html', {
        'advertisements': advertisements
    })


count = 1


class Advertisements(View):

    def get(self, request):
        global count
        count += 1
        advertisements = [
            'Другой мастер на час',
            'Введение в запой',
            'Услуги python-разработчика',
            f'Количество запросов: {count}'
        ]
        return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements})

    def post(self, request):
        advertisements = ['Запрос на создание новой записи выполнен.']
        return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Контактная информация'
        context['title'] = 'Контактная информация'
        context['address'] = """Адрес: г. Ленинград, 3-я улица строителей, дом 25"""
        context['telephone'] = """Телефон: +75645333454"""
        context['email'] = """Эл.почта: irony_fate@mail.ussr"""
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'О компании'
        context['title'] = 'О компании'
        context['description'] = """
        Компания занимается ремонтом в вашей (или нет) квартире, кодированием 1 января.
        Так же помогаем с прогоном гостей после бурного праздника (посредством экскаватора).
        
        За сохранность вашего жилища не отвечаем!
        """
        return context


class Form(TemplateView):
    template_name = 'advertisements/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = """Услуги"""
        context['h1'] = """Выберите услугу"""
        context['category1'] = """Категория 1"""
        context['category2'] = """Категория 2"""
        context['category3'] = """Категория 3"""

        context['region1'] = """Регион 1"""
        context['region2'] = """Регион 2"""
        context['region3'] = """Регион 3"""

        return context
