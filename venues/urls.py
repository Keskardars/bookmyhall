from django.urls import path
from . import views
urlpatterns = [
    path('all_listing',views.venue_list,name='venue_list'),
    path('=$<int:id>',views.venue_detail,name='venue_detail'),
    path('search',views.search,name='search'),
    path('submit_review/<int:id>',views.submit_review,name="submit_review"),
]
