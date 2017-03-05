from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CityForm, WeatherData

from .models import City

import urllib2
import json

# Create your views here.

def home(request):
    cityList = City.objects.all()
    context = {'cities': cityList,}
    if request.method == 'POST':
        #print request.POST
        cityList = City.objects.all()
        form = WeatherData(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            print form.cleaned_data
            f = urllib2.urlopen('http://api.wunderground.com/api/100fda890ffbffd3/geolookup/conditions/q/INDIA/'+city+'.json')
            json_string = f.read()
            parsed_json = json.loads(json_string)
            try:
                location = parsed_json['location']['city']
                temp_f = parsed_json['current_observation']['temperature_string']
                print "Current temperature in %s is: %s" % (location, temp_f)
            except:
                location = "Location not found"
                temp_f = "Unknow"
            f.close()
            context = {'temp':temp_f,'location':location,'cities': cityList}
            return render(request, "home.html", context)
        else:
            return redirect("/")
    else:
        return render(request, "home.html", context)


def addcity(request):
    if request.method == 'POST':
        from .forms import CityForm
        print request.POST
        form = CityForm(request.POST)
        if form.is_valid():
			form.save()
        return redirect("/")
    else:
        return redirect("/")
