from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact, name = 'contact'),
    path('cookies/',views.cookies, name = 'cookies'),
    path('donnees/',views.donnees, name = 'donnees'),
]

