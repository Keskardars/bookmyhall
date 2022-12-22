from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class BannerImage(models.Model):
    highlight_title=models.CharField(max_length=25)
    Title=models.CharField(max_length=300)
    pincode=models.IntegerField(default='413501')
    city=models.CharField(max_length=10,default='Dharashiv')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_date=models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.Title


class Testimonials(models.Model):
    subject=models.CharField(max_length=800)
    image=models.ImageField(upload_to='photos/%Y/%m/%d/')
    couple_name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.couple_name

class Team(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    subject=models.CharField(max_length=400)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
    created_date=models.DateTimeField(auto_now_add=True)
    photograph=models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link=models.URLField(default="",max_length=200)
    twiter_link=models.URLField(default="",max_length=200)
    instagram_link=models.URLField(default="",max_length=200)
    linkdin_link=models.URLField(default="",max_length=200)

    def __str__(self):
        return self.first_name


