"""HR_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from contact_us.views import *
from services.views import *
from HR_management.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('login/',login_hr,name='login'),
    path('logout/',logout_hr,name='logout'),
    path('empdata/',emp_data,name='empdata'),
    path('queries/',emp_queries,name='queries'),
    path('departments/',view_dept,name='dept'),
    path('adddept/',add_dept,name='adddept'),
    path('addemp/',add_emp,name='addemp')    
]
