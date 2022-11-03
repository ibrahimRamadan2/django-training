 
import pytest
from album.models import Album 
from album.serializers import album_serializer
from users.models import Extended_User 
from artist.models import Artist

@pytest.mark.django_db
def test_album_serializer():
    # create user 
    user = Extended_User.objects.create_user(username = "hima" , password = '123123h@')
    # create Artist 
    artist = Artist(stage_name = 'hima' ,  social_link="asdASq@asd.com" , user = user)
    # create an album 
    album =Album(name = 'new hima' , cost =10031.0 , release_at ="2022-10-31T16:15:16Z",
    artist = artist) 
    serializer = album_serializer(album)
   
    assert album.name == serializer.data['name'] 
    assert album.cost == serializer.data['cost'] 
    assert album.release_at == serializer.data['release_at'] 
    assert album.artist.stage_name == serializer.data['artist']['stage_name'] 
    assert album.artist.social_link == serializer.data['artist']['social_link'] 
    
# here i updated the album serializer because it wasn't serialize correctly artist field
# as its forignKey , so i add field artist serializer in alumm serializer (nested serialzer)
# and now i works very good     


 