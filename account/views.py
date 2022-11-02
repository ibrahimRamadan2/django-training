 
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View 
from .forms import newUserForm
from django.contrib.auth import login, authenticate  , logout
from django.contrib.auth.forms import AuthenticationForm #add this
# Create your views here.

class sign_upView(View):
    def get(self , request):
        form  = newUserForm() 
        return render(request , "registration/signup.html" , {'form':form , 'err':2 })
    
    def post(self,  request):
        form = newUserForm(request.POST)
        if(form.is_valid()):
            user =form.save()
            login(request , user)
            return render(request , "registration/signup.html" , {'form':form , 'err':1 })
        return render(request , "registration/signup.html" , {'form':form , 'err':0 })


class loginView(View):
    def get(self , request):
        form = AuthenticationForm()
        return render(request , 'registration/login.html' , {'form':form})
    
    def post(self , request):
        form = AuthenticationForm(request.POST)
        userName = request.POST['username']
        mypassword = request.POST['password']
        print(userName + "  "+mypassword)
        user = authenticate(request, username=userName, password=mypassword)
        if(user is not None):
            login(request, user)
            return render(request , "registration/base.html")
        return HttpResponse("ana m4 tamam yasta ")

class logoutView(View):
    def get(self , request) : 
        logout(request)
        return render(request , "registration/base.html")
    def post(self , request):
        pass


class homeView(View):
    def get(self ,request):
        return render(request, 'registration/base.html')
    
    def post(request):
        pass