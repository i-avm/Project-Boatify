from django.shortcuts import render, redirect
from django.urls import reverse
import pyqrcode
from .models import Seatres, booking
from pyqrcode import QRCode

import stripe
stripe.api_key = "sk_test_g16mqCpueK42qQBfKCkus9UW00JIRkOIIt"

# Create your views here.

def seatres(request):
    if request.method == 'POST':
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        fdate = request.POST.get('fdate')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Date'] = fdate
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
        fdate = request.POST.get('fdate')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Date'] = fdate


        v = request.POST.getlist('checks[]')
        vstr = ""
        count = 0
        for i in v:
            if vstr == "":
                vstr += i
                count+=1
            else:
                vstr += ' - '
                vstr += i
                count+=1

        Dict['Seats'] = vstr
        Dict['Fare'] = int(ffare) * count
        emails = None
        if request.user.is_authenticated:
            emails = request.user.email
        c = Seatres(boatid = boatid, email = emails, seatid=vstr)
        c.save()
        return render(request, 'payment/seatdetails.html', {'W':v, 'print':Dict})
    else:
        return render(request, 'payment/seatdetails.html', {'print': Dict})

def payment(request):
    if request.method == 'POST':
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        fdate = request.POST.get('fdate')
        fseats = request.POST.get('fseats')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['Boatid'] = boatid
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Date'] = fdate
        Dict['Seats'] = fseats
        Dict['Fare'] = ffare
        return render(request, 'payment/paymenthome.html', {'print': Dict})
    else:
        return render(request, 'payment/paymenthome.html')


def charge(request):
    if request.method == 'POST':
        amount = int(request.POST['ffare'])
        email = request.user.email
        name = request.user.username
        customer = stripe.Customer.create(
            email = email,
            name = name,
            source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'inr',
            description = 'Payment by '+request.user.username
        )
        request.idd = customer.id
        boatid = request.POST.get('fboatid')
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        fdate = request.POST.get('fdate')
        fseats = request.POST.get('fseats')

        b = booking(stripe_cusid = customer.id, stripe_chid = charge.id, boatid = boatid, name = name, email = email,
                    seats = fseats, date = fdate, time = ftime, fromm = ffr, to = fto, amount = amount)
        b.save()
        Dict={}
        Dict['Amount'] = amount
        Dict['CusId'] = customer.id
        return render(request, 'payment/paymentstatus.html', {'print': Dict})


#def successMsg(request):
 #   amount = print.Amount
  #  print(amount)
   # return render(request, 'payment/paymentstatus.html', {'amount':amount})


def qrcode(request):
    if request.method == 'POST':
        cusid = request.POST.get('fcusid')
        b = booking.objects.filter(stripe_cusid = cusid)
        current_user = request.user
        s="email="+current_user.email
        url = pyqrcode.create(s)
        url.svg("payment\static\payment\images\qrcode_ticket.svg", scale=8)

        return render(request, 'payment/qrcode.html', {'printqr': b})


def thankyou(request):
    return render(request, 'payment/thankyou.html')