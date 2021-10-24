from django.shortcuts import render
from .models import Jewelry_type, Jewelry


# Create your views here.
def home_view(request):
    jewelry_types = Jewelry_type.objects.all().order_by("name")
    jewelries = Jewelry.objects.filter(star__gt=2).order_by("name")[:6]
    return render(request, 'home.html', {'jewelry_types': jewelry_types, 'jewelries': jewelries})
