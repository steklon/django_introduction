import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    msg = (f'<h2>Текущее время:</h2> {current_time}<br>'
           f'<button style="margin-top: 10px">'
           f'<a href={reverse("home")} style="text-decoration: none">назад</a>'
           f'</button>')
    return HttpResponse(msg)


def workdir_view(request):

    dir_path = os.getcwd()
    files = os.listdir(dir_path)

    html = "<h1>Список файлов в текущей рабочей директории:</h1>"
    html += "<ul>"
    for file in files:
        html += f"<li>{file}</li>"
    html += "</ul>"
    html += (f'<button><a href={reverse("home")} '
             f'style="text-decoration: none">назад</a></button>')

    return HttpResponse(html)
