from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


import users
from users.forms import UserLoginForm

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
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'users/login.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if not all([username, password, password2]):
            return render(request, 'users/reg.html', {'error': 'Please fill in all fields'})

        if password != password2:
            return render(request, 'users/reg.html', {'error': 'Passwords do not match'})


        try:
            user = users.objects.create_user(username=username, password=password)
            user.save()  
            return redirect('login') 
        except Exception as e:
            return render(request, 'users/reg.html', {'error': f'Registration failed: {e}'})

    return render(request, 'users/reg.html')


def profile(request) :
    context =  {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', context)
