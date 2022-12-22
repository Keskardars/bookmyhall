from django.urls import path
from . import views
urlpatterns = [
    path('inquiry',views.inquiry,name='inquiry'),
    path('contact', views.contact_form, name='contact'),
]
