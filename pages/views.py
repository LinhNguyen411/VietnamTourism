from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Region, City, Destination
from django.http import Http404
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class VietNamView(ListView):
    model = Region
    context_object_name = 'region_list' 
    template_name = 'vietnam.html'

def GetRegionObject(region_name):
    for region in Region.objects.all():
        if region.get_normalize_name() == region_name:
            return region
    raise Http404('Region not found')

def GetCityObject(city_name):
    for city in City.objects.all():
        if city.get_normalize_name() == city_name:
            return city
    raise Http404('City not found')

def GetDestinationObject(destination_name):
    for destination in Destination.objects.all():
        print(destination.get_normalize_name())
        if destination.get_normalize_name() == destination_name:
            return destination
    raise Http404('Destination not found')

def RegionDetailView(request, region):
    return render(request, 'region_detail.html',
                context={'region': GetRegionObject(region)})

def CityDetailView(request, region, city):
    region_obj = GetRegionObject(region)
    city_obj = GetCityObject(city)
    if city_obj.region == region_obj:
        return render(request, 'city_detail.html',
                context={'city': city_obj})
    else:
        raise Http404('{} not in {}'.format(city_obj, region_obj))

def DestinationDetailView(request, region, city, destination):
    region_obj = GetRegionObject(region)
    city_obj = GetCityObject(city)
    if city_obj.region == region_obj:
        destination_obj = GetDestinationObject(destination)

        if destination_obj.city == city_obj:
            return render(request, 'destination_detail.html',
                    context={'destination': destination_obj})
        else:
            raise Http404('{} not in {}'.format(destination_obj, city_obj))
    else:
        raise Http404('{} not in {}'.format(city_obj, region_obj))

class SearchView(ListView):
    model = Destination
    context_object_name = 'destination_list'
    template_name = 'search.html'
    def get_queryset(self):
        if len(self.request.GET):
            query = self.request.GET.get('q')
            return Destination.objects.filter(
            name__unaccent__icontains=query)
        else:
            print('hello')
            return Destination.objects.all()