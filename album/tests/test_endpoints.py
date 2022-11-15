import pytest 
from rest_framework.test import APIClient
from album.models import Album
from artist.models import Artist
from users.models import Extended_User

 

# def test_get_approved_albums_GET(auth_client):
#     client  = APIClient()
#     user = Extended_User.objects.create_user(username = 'hima' , password = '123123h@')
#     artist = Artist.objects.create(user = user , stage_name = 'hima' )
#     album1 = Album.objects.create(name = "ablum1" , cost='123'  ,artist =artist ,is_accepted=True) 
#     album2 = Album.objects.create(name = "ablum2" , cost='1233' ,artist =artist ,is_accepted=True) 
#     album3 = Album.objects.create(name = "ablum3" , cost='12333' ,artist =artist ,is_accepted=True) 
#     album_list = [album1, album2, album3]
#     response = client.get('/albums/')
#     data= response.data 
#     for i in range(len(data)):
#         assert data[i]['name'] == album_list[i].name
#         assert data[i]['cost'] == float(album_list[i].cost)
#         assert data[i]['is_accepted'] == album_list[i].is_accepted
#         assert data[i]['artist']['id'] == album_list[i].artist.id
#         assert data[i]['artist']['stage_name'] == album_list[i].artist.stage_name
         
    
    
      
    
def test_get_approved_albums_Post(auth_client,auth_client_artist):
    normal_client = auth_client()  # this is an normal user not an artist 
    response = normal_client.post('/albums/', {
        "name": "tested album22",
        "cost": 123123.0,
        "release_at": "2022-10-31T16:15:16Z"
    } , format ='json')
    assert response.data['error'] == 'the user should be an artist'

    artist_client = auth_client_artist()
    response = artist_client.post('/albums/', {
        "name": "tested album22",
        "cost": 123123.0,
        "release_at": "2022-10-31T16:15:16Z"
    } , format ='json')
    data= response.data 
    assert data['name'] == "tested album22"
    assert data['cost'] == 123123.0
    assert data['release_at'] == "2022-10-31T16:15:16Z"


    # last test : if i try to post same album it will raise error (name must be uniqe)
    response = artist_client.post('/albums/', {
        "name": "tested album22",
        "cost": 123123.0,
        "release_at": "2022-10-31T16:15:16Z"
    } , format ='json')
    print(response.data)
    assert response.data['error'] == 'this album already exist'
    return True 


 