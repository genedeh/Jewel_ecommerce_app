from django.contrib import admin
from .models import Customer, Order, OrderItem, WishList


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    list_display_links = ['name']
    list_editable = ['image']
    search_fields = ['name']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    search_fields = ['name']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WishList, WishListAdmin)
