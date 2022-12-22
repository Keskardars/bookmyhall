from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField #NOTE: That after using ckeditor we have to use {single-car.description |safe for the retriving data safely from the ckeditor after use of |safe the data will be in alignment.Note That!!! }   
from multiselectfield import MultiSelectField
from accounts.models import User
# Create your models here.
class venue(models.Model):
    Type_choice = (
        ('Banquet Hall', 'Banquet Hall'),
        ('Function Hall', 'Function Hall'),
        ('Function / Banquet Hall', 'Function /Banquet Hall'),
    )
    Food_choice=(
        ('Pure_Veg','Pure_Veg'),
        ('Non_Veg','Non_Veg'),
        ('Both','Both')
    )
    
    services=(
        ('Clean Rooms','Clean Rooms'), #[0:7:1]
        ('Free WIFI','Free Wifi'),
        ('Catering','catering'),
        ('Light System','Light System'),
        ('Water supply Free','Water Supply Free'),
        ('Decoration','Decoration'),
        ('Special Menus','Special Menus'),
    )

    menu_list=(
        ('Dessert','Dessert'), #[0:5:1]
        ('North-Indian','North-Indian'),
        ('South-Indian','South-Indian'),
        ('Indian Snacks','Indian Snacks'),
        ('Ice-cream','Ice-cream'),
    )

    people_count=(
        ('1-49','1-49'),     #[0:8:1]
        ('50-99','50-99'),
        ('100-149','100-149'),
        ('149-250','149-250'),
        ('250-399','250-399'),
        ('400-499','400-499'),
        ('500-799','800-999'),
        ('More Than 1000','More than 1000'),
    )

    Aminities=(
        ('VEG AND NON VEG','VEG AND NON VEG'), #[0:5:1]
        ('CAR PARKING LOT','CAR PARKING LOT'),
        ('AC ROOM ','AC ROOM '),
        ('TWO WHEELER PARKING','TWO WHEELER PARKING'),
        ('Concrete Flooring','Concrete Flooring'),
    )

    Hall_rent_cost=(
        ('below 10,000','below 10,000'),
        ('10,000 - 25,000 ','10,000 - 25,000 '),
        ('25,000 - 50,000','25,000 - 50,000'),
        ('50,000 - 75,000 ','50,000 - 75,000 '),
        ('75,000 - 1,00,000','75,000 - 1,00,000'),
        ('1,00,000 -1,50,000 ','1,00,000 -1,50,000 '),
        ('1,50,000 -2,00,000 ','1,50,000 -2,00,000 '),
        ('More than 2,00,000','More than 2,00,000'),
    )
    
    select_event=(
        ('Wedding','Wedding'),
        ('Birthday Party','Birthday Party'),
        ('Engagement','Engagement'),
        ('Naming Ceremony','Naming Ceremony'),
        ('Reception','Reception'),
        ('Anniversary','Anniversary'),
        ('Small Function','Small Functions'),
        ('Other','Other'),
    )


    venue_id=models.IntegerField(unique=True)
    Venue_name=models.CharField(max_length=400)
    Venue_location=models.CharField(max_length=400)
    About=RichTextField()
    phone =models.CharField(max_length=12,null=False,default='')
    type_of_hall=models.CharField(choices=Type_choice,max_length=255)
    Food_type=models.CharField(choices=Food_choice,max_length=50)
    Dining_hall_capacity=models.IntegerField()
    per_plate_prize=models.CharField(max_length=50)
    list_image=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    banner_image1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    banner_image2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    banner_image3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    banner_image4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    extra_image1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    extra_image2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    extra_image3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    map_location=models.URLField(max_length=250,null=True)
    vimeo_video=models.URLField(max_length=250,null=True)
    Parking_capacity=models.IntegerField(default=100)
    Rating=models.FloatField(default=3.0)
    created_date=models.DateTimeField(default=datetime.now)

    Hall_rent_cost=models.CharField(max_length=50,choices=Hall_rent_cost,default='')
    select_event=MultiSelectField(default="Wedding",choices=select_event)
    # multiselect field data
    Aminities=MultiSelectField(default='Two-Whiller Parking',choices=Aminities)
    services=MultiSelectField(default='Decoration',choices=services)
    menus=MultiSelectField(default='Indian Dessert',choices=menu_list)
    people_count=MultiSelectField(default='100',choices=people_count)
    
    #owner details
    owner_name=models.CharField(default='',max_length=100, blank=True)
    about_owner=models.CharField(default='',max_length=250,blank=True )
    open_time=models.CharField(default='24',max_length=50)
    mobile=models.CharField(default='',max_length=12,blank=True)
    email=models.EmailField(default='',max_length=254,blank=True)
    whatsapp_no=models.CharField(default='',max_length=12,blank=True)

     
   #final info
    Total_reviews=models.IntegerField(default='4')
    Response_time=models.FloatField(default='3.0')
    Quality_of_service=models.FloatField(default='3.0')
    Catering_service=models.FloatField(default='2.0')
    Overall_rating=models.FloatField(default='4.0')


class ReviewRating(models.Model):
    venue=models.ForeignKey(venue,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=150,blank=True)
    review=models.TextField(max_length=500,blank=True)
    rating=models.FloatField()
    ip=models.CharField(max_length=20,blank=True)
    status=models.BooleanField(default=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    def __str__(self) :
        return self.subject