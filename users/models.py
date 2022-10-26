from django.db import models

from django.contrib.auth.models import User , AbstractUser
    # Create your models here.



class Extended_User(AbstractUser):
    bio = models.CharField(max_length=254  , blank=True)
     