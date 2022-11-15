import imp
from multiprocessing import managers
from django.contrib import admin
from .models import Album , song
from django import forms
# Register your models here.
class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['isAccepted'].help_text = 'Approve the album if its name is not explicit'
     
class AlbumAdmin(admin.ModelAdmin):
    list_display=("name" , "cost", "isAccepted")
    # readonly_fields=("creationDate",)
    form = MyForm
    
admin.site.register(Album , AlbumAdmin)
admin.site.register(song)

# py manage.py makemigrations