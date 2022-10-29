 
 
import pytest
from rest_framework.test import APIClient
from knox.auth import AuthToken
from users.models import Extended_User
from django.contrib.auth import authenticate
 

@pytest.fixture 
def auth_client(db):
    def get_auth_user(cur_user=None):
        client = APIClient()
        
        if(cur_user is None):
            user = Extended_User.objects.create_user(username= "hima" , password = "123123h@")
            user.save() 
            cur_user = authenticate(username= "hima" , password ="123123h@" )
            
            #get token from login Knox View 
            # this part is already testing the login end point and return : 
            # token : 
            # userData :  
            response = client.post('/authentication/login/' , {
                'username'  : "hima" ,
                'password' : '123123h@',
            } , format='json')
            data =response.data 
            token = data['token']
            #print(data)
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            # return client
            # then test the rest endpoints with this token 

           
        else:
            client.force_authenticate(user = cur_user)
        return client
    return get_auth_user
        