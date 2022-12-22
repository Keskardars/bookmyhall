from django.contrib import admin
from .models import BannerImage,Testimonials,Team
from django.utils.html import format_html

# Register your models here.
class BannerImageAdmin(admin.ModelAdmin):
    list_display=('Title','photo','created_date')
    list_display_links=('Title','photo','created_date')

class TestimonialsAdmin(admin.ModelAdmin):
    def thumb(self,object):
        return format_html ("<img src='{}'width='40' style='border-radius:50px;'/>".format(object.image.url))   
    thumb.short_description="image"

    list_display=('couple_name','created_date','thumb')
    list_display_links=('couple_name',)
    search_fields=('couple_name',)
    list_filter=['couple_name'] 

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html ("<img src='{}'width='40' style='border-radius:50px;'/>".format(object.photograph.url))   
    thumbnail.short_description="photo"

    list_display=('first_name','last_name','thumbnail','created_date')
    list_display_links=('first_name','last_name')
    search_fields=('first_name',) 
    list_filter=['first_name'] 
    
admin.site.register(BannerImage,BannerImageAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Team,TeamAdmin)