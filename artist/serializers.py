from rest_framework import serializers 
from .models import Artist


class Artist_serializer(serializers.ModelSerializer):
    class Meta:
        model = Artist 
        fields='__all__'

    
    def validate(self, attrs):
        return attrs