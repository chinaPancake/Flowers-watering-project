from django import forms
from django.forms import ModelForm
from .models import Flower

# createa a flower from

class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"
