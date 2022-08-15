from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower
# Create your views here.
# request -> respons
# request handler

"""def new_flower(request):
    if request.method == 'POST':
        if request.FLOWER.get('name') and request.FLOWER.get('description') and request.FLOWER.get('frequency') and request.FLOWER.get('amount') and request.FLOWER.get('last_watering') and request.FLOWER.get('next_watering'):
            flower = Flower()
            flower.name = request.FLOWER.get('name')
            flower.description = request.FLOWER.get('description')
            flower.frequency = request.FLOWER.get('frequency')
            flower.amount = request.FLOWER.get('amount')
            flower.last_watering = request.FLOWER.get('last_watering')
            flower.next_watering = request.FLOWER.get('next_watering')
            flower.save()

            return render(request, 'index.html')
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')"""
name = 'Pilea'
description = 'Small oval leafs'
frequency = 7
amount = 250
last_watering = '2022-08-14'
next_watering = '2022-08-21'
def new_flower(request, *args, **kwargs):
    Flower.objects.create(name = name, description = description, frequency = frequency, amount=amount, last_watering = last_watering, next_watering = next_watering )
    query_results = Flower.objects.all()

    context = {'Query_results': query_results}

    return render(request, "index.html", context)