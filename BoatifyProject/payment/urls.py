from django.urls import path
from . import views

urlpatterns = [
    path('', views.paymenthome, name='payment`home'),

    ]
