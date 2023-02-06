from django.contrib import admin
from services.models import *
# Register your models here.
admin.site.register([employees,department])
class empadmin(admin.ModelAdmin):
    list_display=('First_Name','Last_Name','Phone_NO','Joining_Date','Department')
class saladmin(admin.ModelAdmin):
    list_display=('Salary','Department')