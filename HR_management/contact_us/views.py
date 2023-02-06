from django.shortcuts import render,redirect
from django.http import HttpResponse
from contact_us.models import *
from django.core.mail import send_mail

# Create your views here.

def contact(request):
     if request.method=="POST":
          name=request.POST['name']
          email=request.POST['email']
          subj=request.POST['subj']
          phone_no=request.POST['phone_no']
          desc=request.POST['desc']
          if name and email and subj:
               # print(1)
               # send_mail(
               #      subject='This is an AutoResponse from HR department.',
               #      message='This is an autoresponse from our HR department for your email verification. We will conect with you very soon',
               #      from_email='mayankyameto1419@gmail.com',
               #      recipient_list=['m-mayank@hcl.com'],
               #      fail_silently=False
               #      )
               # print(2)
               pass
          cform_data=contform(Name=name,Email=email,Subject=subj,Phone_no=phone_no,Description=desc)
          cform_data.save()
     return render(request,'contact.html')
