from django.urls import path
from . import views
urlpatterns = [
 path('',views.home,name='home'),
 path('about',views.about,name='about'),
 path('banquet_hall',views.banquet_hall,name='banquet_hall'),
 path('byprice_',views.price_by_hall,name='by_price'),
 path('byratings_',views.ratings_page,name='by_rating'),

]