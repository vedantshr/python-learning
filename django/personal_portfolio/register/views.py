from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('User created!')
    else:
        return render(request, 'portfolio/register.html')
    return redirect('/')