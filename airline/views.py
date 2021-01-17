from django.shortcuts import render
from .models import flights
# Create your views here.
def home(request):
    #flights_info=flights.objects.all()
    return render(request,"airline/home.html",{
        "flights":flights.objects.all()
    })

def flight_info(request,flight_id):
    return render(request,"airline/flight_info.html",{
        "flight":flights.objects.get(id=flight_id)
    })