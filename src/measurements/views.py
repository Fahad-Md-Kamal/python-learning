from django.shortcuts import render, get_list_or_404
from geopy.geocoders import Nominatim, Photon
from geopy.distance import geodesic

from .models import Measurement
from .forms import MeasurementModelForm
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

# Create your views here.


def calculate_distance_view(request):
    # initial values
    distance = None
    destination = None

    obj = get_list_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")
    # geolocator = Nominatim(user_agent="measurements")

    # Gets dynamic ip address from the requested user
    # ip_ = get_ip_address(request)
    # print(ip_)

    ip = '103.106.33.98'
    country, city, lat, lon = get_geo(ip)
    # print('location country', country)
    # print('location city', city)
    # print('location lat', lat)
    # print('location lon', lon)

    location = city['city']
    # print('######', location)

    # Location Coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # Initial folium map
    m = folium.Map(
        width=800,
        height=500,
        location=get_center_coordinates(l_lat, l_lon),
        zoom_start=8,
    )
    # location marker
    folium.Marker(
        [l_lat, l_lon],
        tooltip='click here for more',
        popup=city['city'],
        icon=folium.Icon(color='purple')
    ).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        # print(destination)

        # Distance coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)

        # Distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)
        # print(distance)

        # Folium map modification
        m = folium.Map(
            width=800, height=500,
            zoom_start=get_zoom(distance),
            location=get_center_coordinates(
                latA=l_lat,
                longA=l_lon,
                latB=d_lat,
                LongB=d_lon,
            ),
        )

        # location marker
        folium.Marker(
            [l_lat, l_lon],
            tooltip='click here for more',
            popup=city['city'],
            icon=folium.Icon(color='purple')
        ).add_to(m)

        # Destination marker
        folium.Marker(
            [d_lat, d_lon],
            tooltip='click here for more',
            popup=destination,
            icon=folium.Icon(color='red', icon='cloud')
        ).add_to(m)

        # draw the line between location and destination
        line = folium.PolyLine(
            locations=[pointA, pointB],
            weight=5,
            color='blue'
        )
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance': distance,
        'destination': destination,
        'form': form,
        'm': m
    }

    return render(request, 'measurements/main.html', context)
