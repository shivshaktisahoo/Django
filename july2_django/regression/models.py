from django.db import models

# Create your models here.
class Realestatecolmn(models.Model): 
    username = models.CharField(max_length=40)
    house_age = models.FloatField(default=0)
    MRT_station = models.FloatField(default=0)
    con_stores = models.IntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(default=0)
    predicted = models.FloatField(default=0)
    
