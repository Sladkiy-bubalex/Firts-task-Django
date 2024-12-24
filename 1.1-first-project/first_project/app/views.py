import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущая дата и время: {datetime.strftime(current_time, '%d-%m-%Y %H:%M:%S')}'
    return HttpResponse(msg)


def workdir_view(request):
    result = os.listdir(path='.')
    template_name = 'app/work_dir.html'
    return render(request, template_name, {'result': result})
