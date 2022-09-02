from django import forms
from django.forms import ModelForm
from .models import Flower

# createa a flower from

class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"

class BookingForm(forms.Form):
    eventTitle = forms.CharField(label='event', max_length=255, required=True)
    startDateTime = forms.DateField(label='startDateTime', input_formats=['%Y/%m/%d'], required=True)
    endDateTime = forms.DateField(label='endDateTime', input_formats=['%Y/%m/%d'], required=True)
