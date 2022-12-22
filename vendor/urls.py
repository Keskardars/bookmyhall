from django.urls import path
from .import views
urlpatterns = [
   path('vendor-dashboard/',views.vendor_dashboard,name="vendor_dashboard"),
   path('vendor?signup',views.vendorsignup,name='vendorsignup'),
   path('vendor?add_venue',views.add_venue,name='add_venue'),
]
