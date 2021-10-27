from django.urls import path
from .views import home_view, JewelryTypeDetailView, navbar, jewelry_view, JewelryDetailView

app_name = 'Product'

urlpatterns = [
    path('', home_view, name='home'),
    path('jewelry_type/<pk>/', JewelryTypeDetailView.as_view(), name='jewelry_detail'),
    path('navbar/', navbar, name='navbar'),
    path('jewelries/', jewelry_view, name='jewelries'),
    path('<jewelry_type>/<slug>/', JewelryDetailView.as_view(), name='jewelry'),
]
