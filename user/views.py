from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def userdashboard(request):
    return render(request,'accounts/user_dashboard.html')