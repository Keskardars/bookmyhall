from django.shortcuts import render
from pages.models import BannerImage
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from .models import addbusiness
from django.core.mail import send_mail
from bookmyhall import settings
# Create your views here.
def vendor_dashboard(request):
    return render(request,'accounts/vendor_dashboard.html')


def vendorsignup(request):
    pass
    return render(request,'accounts/vendorsignup.html')


def add_venue(request):
    banner_image=BannerImage.objects.all()
    if request.method=='POST':
          location=request.POST.get('location')
          email=request.POST.get('email')
          hall_title=request.POST.get('hall_title')
          google_map_link=request.POST.get('google_map_link')
          image1=request.POST.get('image1')
          image2=request.POST.get('image2')
          image3=request.POST.get('image3')
          image4=request.POST.get('image4')
          celebrate_events=request.POST.get('celebrate_events')
          services_features=request.POST.get('services_features')
          guest_limit=request.POST.get('guest_limit')
          per_plate_rupees=request.POST.get('per_plate_rupees')
          parking_limit=request.POST.get('parking_limit')
          discription=request.POST.get('discription')
          food_type=request.POST.get('food_type')

          addvenue=addbusiness(location=location,email=email,hall_title=hall_title,google_map_link=google_map_link,image1=image1,image2=image2,image3=image3,
                image4=image4,celebrate_events=celebrate_events, services_features=services_features,guest_limit=guest_limit,per_plate_rupees=per_plate_rupees,parking_limit=parking_limit,discription=discription,
                food_type=food_type)

          addvenue.save()
          
          subject = 'Adding Venue Details - From bookmyhall🧧'
          message = f'Hi {request.user.vendor_name} , \n \n This mail is regarding your recent Venue details. your submitted details are Location:{location} \n and inquired at email {email} \n We Wil configured this request and we will transfer your request to Respected Vendor will Contact you Shortly ,please Stay connected with whatsapp\n by bookmyhall <>'
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [email,'darshankeskar900@gmail.com','maindarkarrohan11@gmail.com','amolkumbhar2608@gmail.com']
          send_mail( subject, message, email_from, recipient_list )

    data={
        'banner':banner_image
    }
    return render(request,'accounts/add_venue.html',data)