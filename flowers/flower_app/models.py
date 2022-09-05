from django.db import models
from django.forms import ModelForm


# Create your models here.
class Flower(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=150)
    frequency = models.IntegerField()
    amount = models.IntegerField()
    last_watering = models.DateField()
    next_watering = models.DateField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)