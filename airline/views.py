from django.shortcuts import render,redirect
from .models import flights,passenger
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def home(request):
    #flights_info=flights.objects.all()
    return render(request,"airline/home.html",{
        "flights":flights.objects.all()
    })

def flight_info(request,flight_id):
    flight_detail=flights.objects.get(id=flight_id)
    print(list(flight_detail.passengers.all()))
    return render(request,"airline/flight_info.html",{
        "flight":flight_detail,
        "passengers":flight_detail.passengers.all(),
        "non_passengers":passenger.objects.exclude(planes=flight_detail).all()
    })

def book(request,flight_id):
    if request.method == 'POST':
        flightinfo=flights.objects.get(pk=flight_id)
        passenger_info=passenger.objects.get(pk=int(request.POST['non_passenger']))
        passenger_info.planes.add(flightinfo);
        return redirect('ariline-home')
