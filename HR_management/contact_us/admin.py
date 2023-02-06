from django.contrib import admin
from contact_us.models import *
# Register your models here.
admin.site.register(contform)
class contfadmin(admin.ModelAdmin):
    list_display=('Name','Subject','Email','Phone_no','Description')