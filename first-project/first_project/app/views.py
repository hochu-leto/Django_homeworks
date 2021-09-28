import datetime
import os
from sys import path

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
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
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # filelist = []
    # for root, dirs, files in os.walk():
    #     for file in files:  # append the file name to the list
    #         filelist.append(os.path.join(root,file))    #print all the file names for name in filelist: print(name)
    import pathlib

    msg = ''
    # определение пути
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        msg = msg + str(currentFile) + '\r\n'
    print(msg)

    return HttpResponse(msg)
