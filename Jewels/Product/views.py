from django.shortcuts import render
from django.views.generic import DetailView

from .models import Jewelry_type, Jewelry


# Create your views here.
def home_view(request):
    jewelry_types = Jewelry_type.objects.all().order_by("name")
    jewelries = Jewelry.objects.filter(star__gt=4).order_by("name")[:3]
    return render(request, 'home.html', {'jewelry_types': jewelry_types, 'jewelries': jewelries})


def navbar(request):
    jewelry_types = Jewelry_type.objects.all().order_by("pk")
    get = Jewelry_type.objects.get(pk=2)
    print('-----------------')
    print(get.jewels.name)
    print('-----------------')
    return render(request, 'base.html', {'jewelry_types': jewelry_types})


class JewelryTypeDetailView(DetailView):
    model = Jewelry_type
    template_name = 'Jewelry_Type_detail_page.html'
