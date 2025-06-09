from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('contact/', contact_view, name='contact_view'),
    path('main/', main_view, name='main_view'),
    path('items/', items_view, name='items_view'),
    path('cart/', cart_view, name='cart_view'),
]