from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from PayTm import Checksum

# Create your views here.

MERCHANT_KEY = 'poESoXaHniaGcmKS'


def payment(request):
    if request.method == 'POST':
        ffr = request.POST.get('ffr')
        fto = request.POST.get('fto')
        ftime = request.POST.get('ftime')
        ffare = request.POST.get('ffare')
        Dict = {}
        Dict['From'] = ffr
        Dict['To'] = fto
        Dict['Time'] = ftime
        Dict['Fare'] = ffare
        return render(request, 'payment/paymenthome.html', {'print': Dict})
    else:
        return render(request, 'payment/paymenthome.html')


def paytm(request):
    if request.method == "POST":
        amount = request.POST.get('ffare')

        # order = Orders(name=name, email=email, phone=phone)
        # order.save()
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

            'MID': 'qzcxrB88184026675230',
            'ORDER_ID': '123',
            #'User_Name': User.username,
            'TXN_AMOUNT': str(amount),
            #'CUST_ID': email,
            #'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/payment/handlerequest/',

        }
        #param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        param_dict['CHECKSUMHASH'] = "asdfgh1243567hytgfvcasdfgh1243asdfgh1243asdfgh1243asdfgh1243asdfgh1243asdfgh1243asdfgh1243asdfgh1243asdfgh12"
        return render(request, 'payment/paytm.html', {'param_dict': param_dict})
    else:
        return render(request, 'payment/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    #verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)


    #if verify:
        #if response_dict['RESPCODE'] == '01':
    #        print('order successful')
  #  else:
    #    print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'payment/paymentstatus.html', {'response': response_dict})
