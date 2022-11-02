from django import forms
from .models import Album


class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
         
        labels={
            'name':"your name",
            "cost":"total cost",
        }
        error_messages={
            'name':{
                'required':"type anything ya 8abe"
            }
        }
    def clean_name(self, *args, **kwargs):
        name= self.cleaned_data['name']
        if(len(name) ==0):
            raise forms.ValidationError('Name should not be empty ')
        return name
    def clean_cost(self , *args, **kwargs):
        cost = self.cleaned_data['cost'] 
        if(cost <=0):
            raise forms.ValidationError('cost must be positive value')
        return cost 