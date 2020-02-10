from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome , name='welcome'),
    path('homepage', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('registerpage', views.registerpage, name='registerpage'),
    ]
