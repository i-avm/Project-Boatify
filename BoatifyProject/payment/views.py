from django.shortcuts import render

# Create your views here.

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