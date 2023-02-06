from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from contact_us.models import *
from services.models import *
from services.forms import *

# Create your views here.

@login_required
def services(request):
     return render(request,'services.html')

@login_required
def emp_queries(request):
     queries=contform.objects.all()
     data={'title':'Queries','queries':queries}
     return render(request,'queries.html',data)
@login_required
def add_emp(request):
     if request.POST:
          formdata=addemp(request.POST)
          if formdata.is_valid():
               formdata.save()
               return redirect("empdata")
     return render(request,'addemp.html',{'title':'AddEmp','form':addemp})
@login_required
def emp_data(request):
     emp_data=employees.objects.all()
     data={'title':'EmpData','emp_data':emp_data}
     return render(request,'empdata.html',data)
@login_required
def view_dept(request):
     deptdata=department.objects.all()
     data={'title':'Departments','deptdata':deptdata}
     return render(request,'dept.html',data)
@login_required
def add_dept(request):
     if request.POST:
          formdata=adddept(request.POST)
          if formdata.is_valid():
               formdata.save()
               return redirect("dept")
     return render(request,'adddept.html',{'title':'AddDepartment','form':adddept})