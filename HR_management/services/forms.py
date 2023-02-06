from django.forms import ModelForm
from django import forms
from services.models import *

class addemp(ModelForm):
    class Meta:
        model=employees
        fields='__all__'
class adddept(ModelForm):
    class Meta:
        model=department
        fields='__all__'