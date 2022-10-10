 
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField( max_length=60 , unique=True)
    SocialLink = models.URLField(max_length=300 , blank=True)
    def __str__(self) -> str:
        return f"{self.name}"

 