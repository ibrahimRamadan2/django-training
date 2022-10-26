from django.urls import path
from users import views
from knox import views as knox_views
from  authentication.views import LoginView
urlpatterns = [
    path('register/' , views.Create_user.as_view()),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
