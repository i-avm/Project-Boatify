from django.shortcuts import render, redirect
from .models import Login
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def welcome(request):
    return render(request, 'BoatifyApp/welcome.html')


def homepage(request):
    return render(request, 'BoatifyApp/homepage.html')


def login(request):
    return render(request, 'BoatifyApp/login.html')
def logout(request):
    auth.logout(request)
    return render(request, 'BoatifyApp/homepage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'BoatifyApp/homepage.html')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'BoatifyApp/login.html')
    else:
        return render(request, 'BoatifyApp/login.html')


def registerpage(request):
    if (request.method == 'POST'):
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        username = request.POST.get('uname')
        email = request.POST.get('emailr')
        password_r1 = request.POST.get('pwr1')
        password_r2 = request.POST.get('pwr2')
        if password_r1==password_r2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!!')
                return render(request, 'BoatifyApp/registerpage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken!!')
                return render(request, 'BoatifyApp/registerpage.html')
            else:
                user = User.objects.create_user(username=username, password=password_r1, email=email, first_name=name1, last_name=name2)
                user.save()
                return render(request, 'BoatifyApp/regsuccess.html')
        else:
            messages.info(request, 'Passwords not match .!!')
            return render(request, 'BoatifyApp/registerpage.html')

    else:
        return render(request, 'BoatifyApp/registerpage.html')
