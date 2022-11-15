from .models import Extended_User
from django.contrib import admin
from django import forms

# here i decided to inherit from UserChangeForm class so i can edit user fields widgets . 
# normal inhert from forms.ModelForm and set model attribute to (EXtended_User) doesn't work
from django.contrib.auth.forms import UserChangeForm
class Extended_User_Form(UserChangeForm):
    class Meta:
        model = Extended_User
        fields = '__all__' # required for Django 3.x
        widgets = {
            'bio': forms.Textarea
        }
    
  
