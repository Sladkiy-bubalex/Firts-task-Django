import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination.settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8', newline='') as f:
        reader = list(csv.DictReader(f))

    paginator = Paginator(reader, 10)
    num_page = int(request.GET.get('page', 1))
    page = paginator.get_page(num_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

