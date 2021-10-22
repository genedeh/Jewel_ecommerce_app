from django.contrib import admin
from .models import Jewelry_type, Jewelry


# Register your models here.
class JewelryTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'description']
    search_fields = ['name']
    list_display_links = ['name']
    list_editable = ['picture']


class JewelryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'jewelry_type', 'video', 'star']
    list_display_links = ['name']
    list_editable = ['image', 'video']
    search_fields = ['name', 'star']


admin.site.register(Jewelry_type, JewelryTypeAdmin)
admin.site.register(Jewelry, JewelryAdmin)

# headers and titles
admin.site.site_header = 'JEWELS ADMIN PANEL'
admin.site.site_title = 'JEWELRY SHOP SITE ADMIN'
admin.site.index_title = 'JEWELRY DATA ADMINISTRATION'
