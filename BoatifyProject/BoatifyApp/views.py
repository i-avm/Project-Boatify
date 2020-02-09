from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'BoatifyApp/welcome.html')
def homepage(request):
    return render(request,'BoatifyApp/homepage.html')
def login(request):
    return render(request,'BoatifyApp/login.html')
def register(request):
    return render(request,'BoatifyApp/register.html')
