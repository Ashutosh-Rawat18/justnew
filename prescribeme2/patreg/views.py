# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        pusername = request.POST['username']
        pfirstname = request.POST['firstname']
        plastname = request.POST['lastname']
        pemail = request.POST['email']
        ppassword1 = request.POST['password1']
        ppassword2 = request.POST['password2']

        if ppassword1 == ppassword2:
            user = User.objects.create_user(
                username=pusername, first_name=pfirstname, last_name=plastname, email=pemail, password=ppassword1)
            user.save()
            print("user created")
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'patient_signup.html')
