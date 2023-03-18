from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def log(request):
    if request.method == 'POST':
        username = request. POST['username']
        password = request. POST['password']

        x = auth.authenticate(username=username, password=password)

        if x is not None:
            auth.login(request, x)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('log')

    else:
        return render(request, 'loginchoice.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
