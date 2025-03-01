from django.urls import path
from . import views

urlpatterns = [
    path('events/',views.events, name = 'events'),
    path('offers/',views.offers, name = 'offers'),
    path('sites/',views.sites, name = 'sites'),
    path('sports/',views.sports, name = 'sports'),

]
