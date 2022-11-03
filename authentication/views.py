from pickle import EXT1
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import User_Data_Serializer
from users.models import Extended_User 
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from .serializers import Login_serializer
from rest_framework.response import Response
from users.models import Extended_User 
from knox.models import AuthToken
from django.contrib.auth import authenticate, login
# Create your views here.


class LoginView(APIView):
    authentication_classes = [BasicAuthentication,] 

    def post(self,  request):
        serializer = Login_serializer(data =request.data)
        cur_user = Extended_User.objects.get(username = 'hima')
        data= request.data
        if(serializer.is_valid()):
            # data = request.data 
            # print(data['username'] + " - " + data['password'])
            user = authenticate(username=data['username'] , password= data['password'])
            if(user is not None):
                #print("123123 1 afsf 123 ")
                token =AuthToken.objects.create(user)[1]
                cur_user = Extended_User.objects.get(username = request.data['username'] )
                cur_serializer = User_Data_Serializer(cur_user)
                # login (request , cur_user)
                return Response({ 
                    'token':token  , 
                    'user':  cur_serializer.data  ,  
                     
                })
            print("12312312")
            return Response(serializer.errors  , status.HTTP_400_BAD_REQUEST)
        return Response( serializer.errors, status.HTTP_400_BAD_REQUEST)
 
 




