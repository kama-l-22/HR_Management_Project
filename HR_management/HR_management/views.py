from django.shortcuts import render,redirect
from django.http import HttpResponse
from HR_management.views import *
from django.contrib.auth import login,logout,authenticate
import time

def home(request):
     return render(request,'home.html')
def about(request):
     return render(request,'about.html')
def login_hr(request):
    username,password='',''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_active:
                return redirect('/services')
        else:
            return HttpResponse('<html><body><center><h1 style="margin:200px auto;">User Not Found</h1></center></body></html>')

    return render(request,'login.html')

def logout_hr(request):
    logout(request)
    return redirect('/home')