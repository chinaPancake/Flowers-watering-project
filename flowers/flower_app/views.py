from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic, View

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Flower, User
from datetime import datetime, date, timedelta
from django.views.generic import FormView
from .forms import BookingForm, FlowerForm


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
    if request.method == 'GET':
        flower = Flower.objects.get(pk=request.GET['id'])
        return render(request, 'updateflower.html', {'flower': flower})
    if request.method == 'POST':
        flower = Flower.objects.get(pk=request.POST.get('id'))
        flower.name = request.POST.get('name')
        flower.description = request.POST.get('description')
        flower.frequency = int(request.POST.get('frequency'))
        flower.amount = int(request.POST.get('amount'))
        flower.last_watering = datetime.strptime(request.POST.get('last_watering'),'%Y-%m-%d')
        flower.next_watering = flower.last_watering + timedelta(days=flower.frequency)
        flower.save()
    data = Flower.objects.all()
    flo = {
        'flower_number': data
    }
    return render(request, 'flowerlist.html', flo)

def flower_list(request):
    data = Flower.objects.all()
    flo = {
        'flower_number': data
    }
    return render(request, 'flowerlist.html', flo)

def delete_flower(request):
    data = Flower.objects.all()
    flo = {
        'flower_number': data
    }
    if request.method == 'POST':
        f = Flower()
        f.id = request.POST.get('id')
        Flower.objects.get(id=f.id).delete()
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
    messages.success(request, ("You were logged-out"))
    return redirect('main')


class ListWithForm(View):
    def get(self, request):
        data = Flower.objects.all()
        flo = {
            'flower_number': data
        }
        if request.method == 'POST':
            f = Flower()
            f.name = request.POST.get('name')
            return render(request, 'index.html', flo)
        return render(request, 'index.html', flo)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    sucess_url = reverse_lazy("Login")
    template_name = "signup.html"

class HomeView(FormView):
    form_class = BookingForm
    template_name = 'cal/home.html'