from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower, Post
# Create your views here.
# request -> respons
# request handler

def new_flower(request):
    if request.method == 'POST':
        flower = Flower()
        flower.name = request.POST.get('name')
        flower.description = request.POST.get('description')
        flower.frequency = request.POST.get('frequency')
        flower.amount = request.POST.get('amount')
        flower.last_watering = request.POST.get('last_watering')
        flower.next_watering = request.POST.get('next_watering')
        flower.save()
        return render(request, 'index.html')

    return render(request, 'index.html')
