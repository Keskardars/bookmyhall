from django.db import models
from accounts.models import User,UserProfile
from multiselectfield import MultiSelectField
from datetime import datetime
class vendor(models.Model):
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    user_profile=models.OneToOneField(UserProfile,related_name='userprofile',on_delete=models.CASCADE)
    vendor_name=models.CharField(max_length=50)
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
    

class addbusiness(models.Model):

    celebrate_event=(
      ('Birthday_Party','Birthday_Party'),
      ('Wedding ','Wedding '),
      ('Engagement','Engagement'),
      ('Naming_ceremony','Naming_ceremony'),
      ('Reception','Reception'),
      ('Anniversary','Anniversary'),
      ('Small_Functions','Small_Functions'),
    )
    services_features=(
        ('Decoration','Decoration'),
        ('DJ','DJ'),
        ('Catering','Catering'),
        ('Air_Condition','Air_Condition'),
        ('Free Wifi','Free Wifi'),
        ('Garden','Garden'),
        ('Special-menues',"Special-menues"),
    )

    location=models.CharField(max_length=250,default='')
    email=models.EmailField(max_length=250,default='')
    hall_title=models.CharField(max_length=150,default='',null=True)
    google_map_link=models.URLField(max_length=250,null=True)
    image1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    celebrate_events=MultiSelectField(max_length=100,choices=celebrate_event,blank=True)
    services_features=MultiSelectField(max_length=100,choices=services_features,blank=True)

    guest_limit=models.CharField(max_length=50,default='100')
    per_plate_rupees=models.CharField(max_length=50,default='50')
    hall_cost_per_day=models.CharField(max_length=70,default='1000')
    parking_limit=models.CharField(max_length=50,default='50')
    discription=models.TextField(default="")
    food_type=models.CharField(max_length=70,default='Pure-Veg')
    
    def __str__(self):
        return self.email
    