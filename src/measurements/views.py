from django.shortcuts import render, get_list_or_404
from geopy.geocoders import Nominatim, Photon
from geopy.distance import geodesic

from .models import Measurement
from .forms import MeasurementModelForm
from .utils import get_geo
# Create your views here.


def calculate_distance_view(request):
    obj = get_list_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")

    ip = '103.106.33.98'
    country, city, lat, lon = get_geo(ip)
    # print('location country', country)
    # print('location city', city)
    # print('location lat', lat)
    # print('location lon', lon)

    location = city['city']
    # print('######', location)

    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # geolocator = Nominatim(user_agent="measurements")

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        # print(destination)
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)

        distance = round(geodesic(pointA, pointB).km, 2)
        # print(distance)

        instance.location = location
        instance.distance = distance
        instance.save()

    context = {
        'distance': obj,
        'form': form
    }

    return render(request, 'measurements/main.html', context)
