from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower
from datetime import datetime, date, timedelta
# Create your views here.
# request -> respons
# request handler

def new_flower(request):
    if request.method == 'POST':
        flower = Flower()
        flower.name = request.POST.get('name')
        flower.description = request.POST.get('description')
        flower.frequency = int(request.POST.get('frequency'))
        flower.amount = int(request.POST.get('amount'))
        flower.last_watering = datetime.strptime(request.POST.get('last_watering'),'%Y-%m-%d')
        flower.next_watering = flower.last_watering + timedelta(days=flower.frequency)
        flower.save()
        return render(request, 'index.html')

    return render(request, 'index.html')

def update_flower(request):
    if request.method == 'POST':
        f = Flower.objects.get(name='Pilea')
        f.description = 'dupa'
        f.save()
    return render(request, 'index.html')

def delete_flower(request):
