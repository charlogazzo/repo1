from . import Location
from django.shortcuts import render

def locationSummary(request):
    product_table = Location.locationSummary()
    
    return render(request, 'autoputaway/display.html', product_table)