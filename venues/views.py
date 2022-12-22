from django.shortcuts import render,get_object_or_404,redirect
from .models import venue,ReviewRating
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from pages.models import BannerImage
from .forms import ReviewForm
from django.contrib import messages
# Create your views here.
def venue_list(request):
    halls=venue.objects.order_by('-Rating')
    paginator=Paginator(halls,3)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    data={
        'venue_halls':paged_cars,
    }
    return render(request,'venues/venue_list.html',data)

def venue_detail(request,id):
    venue_detail=get_object_or_404(venue,pk=id)
    reviews =  ReviewRating.objects.filter(venue_id=venue_detail.id)

    data={
        'venue_detail':venue_detail,
        'reviews':reviews,
    }


    return render(request,'venues/venue_detail.html',data)

def search(request):
    venue_search=venue.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            venue_search=venue.objects.filter(About__icontains=keyword)

    if 'event' in request.GET:
        event=request.GET['event']
        if event:
            venue_search=venue.objects.filter(select_event__iexact=event)

    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            venue_search=venue.objects.filter(Venue_location__iexact=state)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            venue_search=BannerImage.objects.filter(city__iexact=city)

    if 'Hallcost' in request.GET:
        Hallcost=request.GET['Hallcost']
        if Hallcost:
            venue_search=venue.objects.filter(Hall_rent_cost__iexact=Hallcost)

    if 'people_count' in request.GET:
        people_count=request.GET['people_count']
        if people_count:
            venue_search=venue.objects.filter(people_count__iexact=people_count)

    if 'Food_type' in request.GET:
        Food_type=request.GET['Food_type']
        if Food_type:
            venue_search=venue.objects.filter(Food_type__iexact=Food_type)



    data={
        'venue_search':venue_search,
        }
    return render(request,'venues/venue_search.html',data)



def submit_review(request,id):
    url=request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews=ReviewRating.objects.get(user__id=request.user.id,venue__id=id)
            form=ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request,'Thank You ! Your Review has been updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.rating=form.cleaned_data['rating']
                data.review=form.cleaned_data['review']
                data.venue_id=id
                data.user_id=request.user.id
                data.save()
                messages.success(request,'Thank You ! Your Review has been submitted!!')
                return redirect(url)

