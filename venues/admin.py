from django.contrib import admin
from . models import venue,ReviewRating
from django.utils.html import format_html

# Register your models here.
class venueAdmin(admin.ModelAdmin):
    def thumb(self,object):
        return format_html ("<img src='{}'width='40' style='border-radius:50px;'/>".format(object.list_image.url))   
    thumb.short_description="image"
    list_display=('thumb','Venue_name','created_date','owner_name','phone','email','whatsapp_no')
    list_display_links=('thumb','Venue_name','created_date','owner_name','phone','email','whatsapp_no')
    search_fields=('Venue_name',)
    list_filter=('Venue_name','owner_name','phone','email','whatsapp_no')

class ReviewRatingAdmin(admin.ModelAdmin):
    list_display=('created_date','venue_id')
    list_display_links=('created_date','venue_id')

admin.site.register(venue,venueAdmin)
admin.site.register(ReviewRating,ReviewRatingAdmin)
