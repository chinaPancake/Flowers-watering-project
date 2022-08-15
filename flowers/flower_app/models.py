from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length= 25, primary_key=True)
    description = models.CharField(max_length=150)
    frequency = models.IntegerField()
    amount = models.IntegerField()
    last_watering = models.DateField()
    next_watering = models.DateField()