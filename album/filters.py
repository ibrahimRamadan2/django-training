import django_filters 
from .models import Album


class Album_List_Filter(django_filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'name':['icontains'], 
            'cost':['lte' , 'gte'],
            
        }