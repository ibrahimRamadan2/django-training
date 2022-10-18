from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    stageName = forms.CharField(required=False , max_length=100)
    SocialLink = forms.EmailField(required=False , max_length=254)
    class Meta: 
        model = Artist
        fields='__all__'
    
    def clean_stageName(self ,*args, **kwargs):
        name = self.cleaned_data['stageName'] 
         
        if(len(name.strip()) == 0):
            return forms.ValidationError("Name should not be empty")
        return name

