from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import pyqrcode
from .models import Seatres
from pyqrcode import QRCode

import stripe

stripe.api_key = "sk_test_g16mqCpueK42qQBfKCkus9UW00JIRkOIIt"

# Create your views here.




def payment(request):
    if request.method == 'POST':
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Fare'] = ffare
        return render(request, 'payment/paymenthome.html', {'print': Dict})
    else:
        return render(request, 'payment/paymenthome.html')

def seatres(request):
    if request.method == 'POST':
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Fare'] = ffare

        return render(request, 'payment/seatres.html', {'print': Dict})
    else:
        return render(request, 'payment/seatres.html', {'print': Dict})

def seatdetails(request):
    if request.method == 'POST':
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Fare'] = ffare

        v = request.POST.getlist('checks[]')
        vstr = ""
        for i in v:
            vstr += i
            vstr += '-'
        Dict['v'] = vstr
        #emails = User.objects.filter(is_active = True).values_list('email')
        emails = None
        if request.user.is_authenticated:
            emails = request.user.email
        c = Seatres(boatid = boatid, email = emails, seatid=vstr)
        c.save()
        return render(request, 'payment/seatdetails.html', {'W':v, 'print':Dict})
    else:
        return render(request, 'payment/seatdetails.html', {'print': Dict})

def qrcode(request):
    # String which represent the QR code
    #s = "www.geeksforgeeks.org"
    current_user = request.user
    s="email="+current_user.email
    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the png file naming "myqr.png"
    url.svg("payment\static\payment\images\qrcode_ticket.svg", scale=8)
    return render(request, 'payment/qrcode.html')

def charge(request):
    if request.method == 'POST':
        print('data: ',request.POST)

        amount = int(request.POST['ffare'])

        customer = stripe.Customer.create(
            email = request.user.email,
            name = request.user.username,
            source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'inr',
            description = 'Payment by '+request.user.username
        )

    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'payment/paymentstatus.html', {'amount':amount})
