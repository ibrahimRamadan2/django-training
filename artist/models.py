  
from django.db import models
from users.models import Extended_User
# Create your models here.

class Artist(models.Model):
    
    user = models.ForeignKey(Extended_User , on_delete=models.CASCADE ,null=True)
    stage_name = models.CharField(max_length=250 , unique= True)
    social_link = models.CharField( max_length=150 , blank= True)
    def __str__(self) -> str:
        return f"{self.stage_name}"


    