from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


import users
from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user :
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context =  {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def reg(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
           form.save()
           user = form.instance
           auth.login(request, user)
        return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context =  {
        'title': 'Регистрация'
    }
    return render(request, 'users/reg.html', context)


def profile(request) :
    context =  {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', context)
