from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from django.views.generic import DetailView
from django.db.models.functions import Lower
from datetime import datetime

data = {
    'title':0,
}

def index(request):
    data['title'] = 'ТЗ Python'
    return render(request, 'main/index.html', data, status=status.HTTP_200_OK)

def cities(request):
    city = City.objects.all().order_by(Lower('cityName'))
    data['title'] = 'Города'
    data['cities'] = city
    return render(request, 'main/cities.html', data, status=status.HTTP_200_OK)

def findshop(request):
    return render(request, 'main/findshop.html', status=status.HTTP_200_OK)

def shop(request):
    data['title'] = 'Магазины'
    if request.method == 'GET':
        req = []

        city = request.GET.get("city", "")
        street = request.GET.get("street", "")
        open = request.GET.get("open", "")
        currtime = datetime.now().time()

        shops = Shop.objects.all()
        if city != "" or street != "" or open == "on":
            for shop in shops:
                if city != "":
                    if shop.shopCity.lower() == city.lower():
                        req.append(shop)
                elif street != "":
                    if shop.shopStreet.lower() == street.lower():
                        req.append(shop)
                elif open == 'on':
                    if shop.shopTO.hour <= int(currtime.hour) and shop.shopTC.hour >= int(currtime.hour):
                        #if shop.shopTO.minute <= int(currtime.minute) and shop.stopTC.minute >= int(currtime.minute):
                        req.append(shop)

            for shop in req:
                if city != "":
                    if shop.shopCity.lower() != city.lower():
                        req.remove(shop)
                if street != "":
                    if shop.shopStreet.lower() != street.lower():
                        req.remove(shop)

            data['shops'] = req
        else:
            data['shops'] = shops
        return render(request, 'main/shop.html', data, status=status.HTTP_200_OK)

    shops = Shop.objects.all()
    data['shops'] = shops
    return render(request, 'main/shop.html', data, status=status.HTTP_200_OK)

def createshop(request):
    return render(request, 'main/createshop.html', status=status.HTTP_200_OK)

def addShop(request):
    if request.method == 'POST':
        form = Shop()
        form.shopName = request.POST.get('shopName')
        form.shopCity = request.POST.get('shopCity')
        form.shopStreet = request.POST.get('shopStreet')
        form.shopHouse = request.POST.get('shopHouse')
        form.shopTO = request.POST.get('shopTO')
        form.shopTC = request.POST.get('shopTC')
        form.save()
    return HttpResponseRedirect("/createshop")

class CityStreet(DetailView):
    model = City
    context_object_name = 'city'