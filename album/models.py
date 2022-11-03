from datetime import datetime
from django.db import models
from artist.models import Artist
from model_utils.models import TimeStampedModel
# Create your models here.
 
 
class Album(TimeStampedModel):
    # now this model has 2 attrs from timeStamp model
    # 1 - created  (when this obj in created )
    # 2-  modified (when last save has done to this obj)

    name = models.CharField(blank=True, max_length=100, default="New Album")
    cost = models.FloatField()
    release_at = models.DateTimeField(
        default=datetime.now(), auto_now=False, auto_now_add=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return  f"{self.name}"
   
    class Meta:
        ordering = ('name',)





 