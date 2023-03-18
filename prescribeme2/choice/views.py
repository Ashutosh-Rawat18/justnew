from django.shortcuts import render

# Create your views here.


def choice(request):
    return render(request, 'signup_page.html')
