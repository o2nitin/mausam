from django import forms
from django.forms import ModelForm
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City


class WeatherData(forms.Form):
    city = forms.CharField()
    date = forms.CharField()
