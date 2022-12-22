from django.shortcuts import render,redirect,get_object_or_404
from .models import Inquiry,contact
from django.contrib import messages
from venues.models import venue
from accounts.models import User,UserProfile
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from bookmyhall import settings

# Create your views here.

@login_required(login_url='login')
def inquiry(request):
    if request.method == "POST":
        inquiry_id=request.POST.get('inquiry_id')
        user_id=request.POST.get('user_id')
        venue_name = request.POST.get('venue_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        date = request.POST.get('date')
        event_type = request.POST.get('event_type')
        guest_count = request.POST.get('guest_count')
        hall_cost_range = request.POST.get('hall_cost_range')
        note = request.POST.get('note')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Inquiry.objects.all().filter(inquiry_id=inquiry_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an enquiry this Hall.please wait until Our reply!!")
                return redirect('/venue/=$'+inquiry_id)

        inquiry = Inquiry(venue_name= venue_name, name=name , email=email ,phone_no=phone_no,guest_count=guest_count, hall_cost_range=hall_cost_range ,note=note,date=date,event_type=event_type,inquiry_id=inquiry_id,user_id=user_id)
        inquiry.save()
        subject = 'Inquiry about venue - From bookmyhall🧧'
        message = f'Hi {name} , \n \n This mail is regarding your recent Inquiry . your submitted details are phone no :{phone_no} \n and inquired at date {date} \n We Wil configured this request and we will transfer your request to Respected Vendor will Contact you Shortly ,please Stay connected with whatsapp\n by bookmyhall <>'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,'darshankeskar900@gmail.com','maindarkarrohan11@gmail.com','amolkumbhar2608@gmail.com']
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request,"Your request has been submitted,Please check out Mail .We will get back with replay shortly!!!")
        return redirect('/venue/=$'+inquiry_id)



def contact_form(request):
    if request.method =='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contacts=contact(full_name=full_name,email=email,subject=subject,message=message)
        contacts.save()
       
        subject ='You have a new message from bookmyhall website regarding'+subject
        email_from = settings.EMAIL_HOST_USER
        message =f'Got a contact message from {full_name} \n and email {email}\n and subject {subject} \n and message is {message},\n \n thats all. check it and configured it soon as possible.\n \n by bookmyhall'
        recipient_list = ['darshankeskar900@gmail.com','maindarkarrohan11@gmail.com','amolkumbhar2608@gmail.com']
        send_mail(subject, message ,email_from,recipient_list)

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    return render(request,'pages/contact.html')

    