from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Главная ',
    }
    return render(request, 'main/index.html',context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас ',
        'text_on_page': 'Магазин классный'
    }
    return render(request, 'main/about.html',context)