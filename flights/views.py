from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect

from .forms import FlightForm
from .models import Flight

from django.db.models import Avg
from .models import Flight

def index(request):
    return render(request, 'base.html')


def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
    else:
        form = FlightForm()
    return render(request, 'register_flight.html', {'form': form})



def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'list_flights.html', {'flights': flights})



def flight_statistics(request):
    national_flights = Flight.objects.filter(flight_type='Nacional').count()
    international_flights = Flight.objects.filter(flight_type='Internacional').count()
    average_price_national = Flight.objects.filter(flight_type='Nacional').aggregate(Avg('price'))['price__avg']

    return render(request, 'flight_statistics.html', {
        'national_flights': national_flights,
        'international_flights': international_flights,
        'average_price_national': average_price_national,
    })

