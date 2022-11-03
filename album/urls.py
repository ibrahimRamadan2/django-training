from django.urls import path , include
from  . import views

urlpatterns = [
    path('' ,views.get_approved_albums.as_view()) , 
    path('2/' , views.get_approved_albums2.as_view()) , 
]
