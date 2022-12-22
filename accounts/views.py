from django.shortcuts import render,redirect
from .forms import UserForm
from vendor.forms import vendorForm
from .models import User,UserProfile
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib import auth
from .utils import detectUser
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from contact.models import Inquiry
from venues.models import venue
from vendor.models import vendor

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.

# restrict the user from accessing the vendor page
def check_role_vendor(user):
  if user.role == 1:
    return True
  else:
    raise PermissionDenied


# restrict the user from accessing the customer page
def check_role_customer(user):
  if user.role == 2:
    return True
  else:
    raise PermissionDenied




def register_User(request):
  if request.user.is_authenticated:
       messages.warning(request,"You are already logged in!")
       return redirect('user_dashboard')
  elif request.method=='POST':
      form=UserForm(request.POST)
      if form.is_valid():
        # password=form.cleaned_data['password']
        # user=form.save(commit=False)
        # user.set_password(password)
        # user.role=User.customer
        # user.save()
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        email=form.cleaned_data['email']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.role=User.CUSTOMER
        user.save()
        # user activation
        current_site=get_current_site(request)
        mail_subject="Please Activate Your Account"
        message=render_to_string('accounts/account_verification_email.html',{
         'user':user,
         'domain':current_site,
         'uid':urlsafe_base64_encode(force_bytes(user.pk)), #encoding id after that we will decode
         'token':default_token_generator.make_token(user),
        })
        to_email=email
        send_email=EmailMessage(mail_subject,message,to=[to_email])
        send_email.send()

        messages.success(request,"Thank You for registering with us ! We have sent a Verifiation Mail to your email address Please verify Your account before you login.")
        return redirect('/accounts/login/?command=verification&email=' + email)
  else:    
      form=UserForm()
  context={
    'form':form,
    }
  return render(request,'accounts/user_signup.html',context)

def register_vendor(request):
    if request.user.is_authenticated:
      messages.warning(request,"You are already logged in!")
      return redirect('myaccount')
    elif request.method == "POST":
        form = UserForm(request.POST)
        v_form = vendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
          # first_name=form.cleaned_data['first_name']
          # last_name=form.cleaned_data['last_name']
          # password=form.cleaned_data['password']
          # email=form.cleaned_data['email']
          # user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password)
          # user.role=User.vendor
          # user.save()
          # vendor=vendor_form.save(commit=False)
          # vendor.user=user
          # user_profile=UserProfile.objects.get(user=user)
          # vendor.user_profile=user_profile
          # user.save()
          first_name = form.cleaned_data['first_name']
          last_name = form.cleaned_data['last_name']
          email = form.cleaned_data['email']
          username=form.cleaned_data['username']
          password = form.cleaned_data['password']
          user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password)
          user.role = User.VENDOR
          user.save()

          vendor = v_form.save(commit=False)
          vendor.user = user
          vendor_name = v_form.cleaned_data['vendor_name']
          vendor.vendor_slug = slugify(vendor_name)+'-'+str(user.id)
          user_profile = UserProfile.objects.get(user=user)
          vendor.user_profile = user_profile
          vendor.save()

          # user activation
          current_site=get_current_site(request)
          mail_subject="Please Activate Your Account"
          message=render_to_string('accounts/account_verification_email.html',{
          'user':user,
          'domain':current_site,
          'uid':urlsafe_base64_encode(force_bytes(user.pk)), #encoding id after that we will decode
          'token':default_token_generator.make_token(user),
           })
          to_email=email
          send_email=EmailMessage(mail_subject,message,to=[to_email])
          send_email.send()
          return redirect('/accounts/login/?command=verification&email=' + email)
    else:    
        form=UserForm()
        v_form=vendorForm()
    context={
    'form':form,
    'v_form':v_form,
    }
    return render(request,'accounts/vendor_signup.html',context)


def login(request):
  if request.user.is_authenticated:
    messages.warning(request,"You are already logged in!")
    return redirect('myaccount')

  elif request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user=auth.authenticate(email=email,password=password)

    if user is not None:
        auth.login(request,user)
        messages.success(request,"You are now Logged In!!")
        return redirect('myaccount')
    else:
        messages.error(request,"Invalid Login Credentials")
        return redirect('login')
  return render(request,'accounts/login.html')

  
def logout(request):
  auth.logout(request)
  return redirect('login')


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def userdashboard(request):
  user_inquiry=Inquiry.objects.order_by('-created_date').filter(user_id = request.user.id)
  context={
    'user_inquiry':user_inquiry,
  }
  return render(request,'accounts/user_dashboard.html',context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendordashboard(request):
  Vendor = vendor.objects.get(user=request.user)
  inquiry = Inquiry.objects.filter(inquiry_id__in = [Vendor.user.id]).order_by('created_date')
  context={
    'vendor_inquiry': inquiry,
  }
  return render(request,'accounts/vendor_dashboard.html',context)


@login_required(login_url='login')
def myaccount(request):
  user=request.user
  redirectUrl = detectUser(user)
  return redirect(redirectUrl)

def activate(request,uidb64,token):
  try:
    uid=urlsafe_base64_decode(uidb64).decode()
    user=User._default_manager.get(pk=uid)
  except(TypeError,ValueError,OverflowError,User.DoesNotExist):
    user=None
  
  if user is not None and default_token_generator.check_token(user,token):
    user.is_active =True
    user.save()
    messages.success(request,"Congratulations ! your account is activated.")
  else:
    messages.error(request,"Invalid  Activation Link!! Try again")
  return redirect('login')