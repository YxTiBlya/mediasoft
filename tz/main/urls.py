from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('city/', cities, name = 'cities'),
    path('createshop/', createshop, name='createshop'),
    path('findshop/', findshop, name='findshop'),
    path('findshop/shop/', shop, name='shop'),
    path('createshop/addShop/', addShop),
    path('city/<int:pk>/street', CityStreet.as_view(), name = 'street')
]