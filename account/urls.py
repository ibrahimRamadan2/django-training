from django.urls import path , include
from . import views
urlpatterns = [
    path('sign-up', views.sign_upView.as_view()), 
    path('login-user', views.loginView.as_view()) , 
    path('logout-user', views.logoutView.as_view()) , 
    path('',views.homeView.as_view()),
]
