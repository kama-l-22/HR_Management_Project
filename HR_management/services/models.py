from django.db import models

# Create your models here.
class employees(models.Model):
    First_Name=models.CharField(max_length=15)
    Last_Name=models.CharField(max_length=50)
    Phone_NO=models.BigIntegerField()
    Joining_Date=models.DateField(auto_now=False, auto_now_add=False)
    Designation=models.CharField(max_length=50)

class department(models.Model):
    Department=models.CharField(max_length=50)
    Salary=models.IntegerField()


    