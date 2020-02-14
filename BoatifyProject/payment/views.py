from django.shortcuts import render

# Create your views here.

def paymenthome(request):
    return render(request, 'payment/paymenthome.html')