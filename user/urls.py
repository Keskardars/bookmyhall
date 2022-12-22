from django.urls import path,include
from .import views
urlpatterns = [
   path('user/',include('accounts.urls')),
   path('u?dashboard',views.userdashboard,name='user_dashboard')

]
