from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    stage_name = forms.CharField(required=False , max_length=100)
    SocialLink = forms.EmailField(required=False , max_length=254)
    class Meta: 
        model = Artist
        fields='__all__'
    
    def clean_stage_name(self ,*args, **kwargs):
        name = self.cleaned_data['stage_name'] 
         
        if(len(name.strip()) == 0):
            return forms.ValidationError("Name should not be empty")
        return name

