from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Flower, User
from datetime import datetime, date, timedelta
# Create your views here.
# request -> respons
# request handler

def main(request):
    return render(request, 'index.html')

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
        return render(request, 'addflower.html')

    return render(request, 'addflower.html')

def update_flower(request):
    data = Flower.objects.all()
    flo = {
        'flower_number': data
    }
    if request.method == 'POST':
        f = Flower()
        f.name = request.POST.get('name')
        return render(request, 'updateflower.html', flo)
    return render(request, 'updateflower.html', flo)

def delete_flower(request):
    data = Flower.objects.all()
    flo = {
        'flower_number': data
    }
    if request.method == 'POST':
        f = Flower()
        f.name = request.POST.get('name')
        Flower.objects.get(name=f.name).delete()
        return render(request,'deleteflower.html',flo)
    return render(request, 'deleteflower.html', flo)

def login_user(request):
    if request.method == 'POST':
        pass
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request, ("There was an error login... Try again!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were loge Out"))
    return redirect('main')