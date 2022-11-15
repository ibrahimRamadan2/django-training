from rest_framework import serializers
from .models import Album
from artist.models import Artist
from users.serializers import User_Serializer
from artist.serializers import Artist_serializer
class album_serializer(serializers.ModelSerializer):
    artist = Artist_serializer(required = False)
    class Meta:
        model =Album 
        fields = '__all__'

     
    def create(self, validated_data , artist_data):
        album =Album.objects.create(**validated_data , artist=artist_data )               
        return album

    def validate_artist(self, value):
        raise serializers.ValidationError("1313123123123")
        return value
           
     