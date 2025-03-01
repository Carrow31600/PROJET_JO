from django.shortcuts import render

def events(request):
    return render (request,'catalog/events.html')

def offers(request):
    return render (request,'catalog/offers.html')

def sites(request):
    return render (request,'catalog/sites.html')

def sports(request):
    return render (request,'catalog/sports.html')


