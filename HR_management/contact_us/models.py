from django.db import models


# Create your models here.
class contform(models.Model):
    Name=models.CharField(max_length=15)
    Subject=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone_no=models.IntegerField()
    Description=models.TextField(max_length=100)

