 
from django.db import models
import datetime
# Create your models here.
class Artist(models.Model):
    stageName = models.CharField( max_length=60 , unique=True)
    SocialLink = models.URLField(max_length=300 , blank=True)
    def __str__(self) -> str:
        return f"{self.stageName}"
    class Meta : 
        ordering = ('stageName',)
        
 