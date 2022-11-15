from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:pk>', views.Get_User_Details.as_view() ) , 
]
