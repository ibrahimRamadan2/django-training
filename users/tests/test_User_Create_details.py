 
import re
import pytest
from rest_framework.test import APIClient ,RequestsClient
 
from users.models import Extended_User

 


def test_Create_User(db):
    client = APIClient()

    response = client.post('/authentication/register/' ,{
        "username":"ahmedMorgan2222" ,
        "email":"asdasd@asd.com", 
        "password1":"123123h@" ,
        "password2": "123123h@"  
        }, format='json')
    
    user = {
         "username":"ahmedMorgan2222" ,
        "email":"asdasd@asd.com", 
        "password":"123123h@" , 
    }
    data =response.data
    assert data['username'] == user['username']
    assert data['email'] == user['email']
    
    

# here you have to be register to read only  data
# you have to be he owner to edit the data  
def test_Get_User_Details(auth_client):
    client = auth_client()
    response = client.get('/user/1')
    # print(response.data)
    user = Extended_User.objects.get(id = 1) 
    data = response.data 
    assert user.username == data['username']
    assert user.email == data['email']
    assert user.bio == data['bio']
        



def test_Edit_User_Details(auth_client):
    client = auth_client()
    response = client.put('/user/1' , {
        "username":"hima", 
        "email":"hh@asd.com", 
        "bio":"update is done ", 
    } , format='json')
    correct_response={
        'msg': 'user has updated successfully', 
        'id': 1,
        'username': 'hima', 
        'email': 'hh@asd.com', 
        'bio': 'update is done',
        }

    data =response.data
    assert correct_response['msg'] ==  data['msg']
    assert correct_response['username'] ==  data['username']
    assert correct_response['email'] ==  data['email']
    assert correct_response['bio'] ==  data['bio']
     
     
 
    
