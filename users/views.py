from .serializers import User_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from knox.auth import TokenAuthentication   
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import BasicAuthentication
from users.models import Extended_User
from users.serializers import User_Data_Serializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class Create_user(APIView):
    def get(self , request):
        pass

    def post(self , request):
        data=request.data 
        if(data['password1']!= data['password2']):
            return Response({'Error_Message' : "password doesn't match"}, status.HTTP_400_BAD_REQUEST)
        serializer= User_Serializer(data={**data , 'password':data['password1']})
        if(serializer.is_valid()):
            serializer.save()
            return Response( serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors ,status.HTTP_400_BAD_REQUEST)
        


class Get_User_Details(APIView): 
    authentication_classes =[TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly,]
    
    def get(self , request, pk):
        try:
            cur_user = Extended_User.objects.get(id= pk)
            serializer = User_Data_Serializer(cur_user)
            return Response(serializer.data)
        except:
            return Response({"msg":"this user does not exist"} , status.HTTP_404_NOT_FOUND)
    def put(self , request, pk):
        # try:
        cur_user = Extended_User.objects.get(id= pk)
         
        self.check_object_permissions(self.request, cur_user)
        serializer = User_Data_Serializer(cur_user , data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"msg":"user has updated successfully" , **serializer.data} , 
            status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status.HTTP_404_NOT_FOUND) 
        # except:
        #     return Response({"msg":"this user does not exist"} , status.HTTP_404_NOT_FOUND)
 



