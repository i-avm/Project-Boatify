from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('paytm', views.paytm, name='paytm'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    ]
