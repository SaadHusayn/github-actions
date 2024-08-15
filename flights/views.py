from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })

def displayFlightInformation(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id)
    except:
        raise Http404()
    
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["foo"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:displayFlightInformation", args=(flight.id, )))
    
