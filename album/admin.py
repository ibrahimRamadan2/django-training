from django.contrib import admin
from .models import Album
from django import forms
# Register your models here.
class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['isAccepted'].help_text = 'Approve the album if its name is not explicit'

class AlbumAdmin(admin.ModelAdmin):
    list_display=("name" , "cost",'artist' ,  "is_accepted")

   

admin.site.register(Album , AlbumAdmin)