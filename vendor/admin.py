from django.contrib import admin
from .models import vendor,addbusiness
class VendorAdmin(admin.ModelAdmin):
    list_display=('user','vendor_name','is_approved','created_at')
    list_display_links=('user','vendor_name')

class addbusinessAdmin(admin.ModelAdmin):
    list_display=('email','hall_title')
    list_display_links=('email','hall_title')

admin.site.register(vendor,VendorAdmin)
admin.site.register(addbusiness,addbusinessAdmin)