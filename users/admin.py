 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Extended_User
from .forms import Extended_User_Form
# Register your models here.
class Custom_User_Admin(UserAdmin):
    form=Extended_User_Form
    fieldsets=[
        *UserAdmin.fieldsets , 
        ('bio field' ,{
            'fields':('bio',)
        })
    ]
admin.site.register(Extended_User , Custom_User_Admin)

