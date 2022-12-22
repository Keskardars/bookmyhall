from django.db import models
from datetime import datetime
from venues.models import venue
# Create your models here.
class Inquiry(models.Model):
    user_id=models.IntegerField(default=None,unique=True)
    inquiry_id=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    venue_name=models.ForeignKey(venue,on_delete=models.CASCADE,blank=True,null=True)
    phone_no=models.CharField(max_length=12)
    date=models.DateTimeField()
    event_type=models.CharField(max_length=50)
    guest_count=models.CharField(max_length=200)
    hall_cost_range=models.CharField(max_length=100)
    note=models.TextField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)
     
    def __str__(self):
        return self.email


class contact(models.Model):
    full_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=200)
    subject=models.TextField()
    created_date=models.DateTimeField(blank=True,default=datetime.now)
    def __str__(self):
        return self.full_name