from django.contrib import admin
from .models import Inquiry,contact
# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_display=('email','name','created_date','phone_no')
    list_display_links=('email','name','created_date','phone_no')
    search_fields=('name','email')
    list_per_page=25


class contactAdmin(admin.ModelAdmin):
    list_display=('email','full_name','created_date')
    list_display_links=('email','full_name','created_date')
    search_fields=('name','email')
    list_per_page=25

admin.site.register(Inquiry,InquiryAdmin)
admin.site.register(contact,contactAdmin)