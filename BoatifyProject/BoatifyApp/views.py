from django.shortcuts import render
from .models import Login


# Create your views here.
def welcome(request):
    return render(request, 'BoatifyApp/welcome.html')


def homepage(request):
    return render(request, 'BoatifyApp/homepage.html')


def login(request):
    return render(request, 'BoatifyApp/login.html')


def registerpage(request):
    if (request.method == 'POST'):
        name_r = request.POST.get('namer')
        email_r = request.POST.get('emailr')
        password_r = request.POST.get('pwr')

        c = Login(name=name_r, email=email_r, password=password_r)
        c.save()
        return render(request, 'BoatifyApp/regsuccess.html')
    else:
        return render(request, 'BoatifyApp/registerpage.html')
