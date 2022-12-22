from django.urls import path
from. import views
urlpatterns = [
    path('user_register',views.register_User,name='user_register'),
    path('vendor_register',views.register_vendor,name='vendor_register'),

    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('Userdashboard/',views.userdashboard,name='user_dashboard'),
    path('vendordashboard/',views.vendordashboard,name='vendor_dashboard'),

    path('activate/<uidb64>/<token>/',views.activate,name='activate')
]
