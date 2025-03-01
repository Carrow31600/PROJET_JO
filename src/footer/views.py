from django.shortcuts import render

def contact(request):
    return render (request,'footer/contact.html')

def cookies(request):
    return render (request,'footer/cookies.html')

def donnees(request):
    return render (request,'footer/donnees.html')