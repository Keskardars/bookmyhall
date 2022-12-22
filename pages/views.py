from django.shortcuts import render
from .models import BannerImage,Testimonials,Team
from venues.models import venue
# Create your views here.

def home(request):
    banner_image=BannerImage.objects.all()
    testimonials=Testimonials.objects.all()
    best_halls=venue.objects.order_by('-Rating')
    By_pricing=venue.objects.all().order_by('per_plate_prize')
    By_Type_of_hall=venue.objects.all().order_by('type_of_hall')
    # search_fields=banner_image.values('city')
    city_search=BannerImage.objects.values_list('city',flat=True).distinct()
    # search_fields=venue.objects.values('Food_type','Hall_rent_cost')
    Food_type_search=venue.objects.values_list('Food_type',flat=True).distinct()
    Hall_rent_cost=venue.objects.values_list('Hall_rent_cost',flat=True).distinct()
    data={
        'banner':banner_image,
        'testmonial':testimonials,
        'best_halls':best_halls,
        'By_pricing':By_pricing,
        'By_Type_of_Hall':By_Type_of_hall,
        'city_search':city_search,
        'Food_ype_search':Food_type_search,
        'Hall_rent_cost':Hall_rent_cost,
    }
    return render(request,'pages/home.html',data)


def about(request):
    team=Team.objects.all()
    data={
        'teams':team,
    }
    return render(request,'pages/about.html',data)

def contact(request):
    return render(request,'pages/contact.html')


def banquet_hall(request):
    banquet_hall=venue.objects.filter(type_of_hall='Banquet Hall')
    context={
        'banquet_hall':banquet_hall,
    }
    return render(request,'pages/banquet_hall.html',context)

def price_by_hall(request):
    By_pricing=venue.objects.all().order_by('per_plate_prize')
    context={
        'by_pricing':By_pricing,
    }
    return render(request,'pages/price_by_hall.html',context)


def ratings_page(request):
    best_halls=venue.objects.order_by('-Rating')
    context={
        'by_rating':best_halls,
    }
    return render(request,'pages/by_ratings.html',context)

