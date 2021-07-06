from django.db import models

# Create your models here.
class Vacationtrip(models.Model): 
    first_name = models.CharField(max_length=40,default="")
    last_name = models.CharField(max_length=40,default="")
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=40,default="")
    contactno = models.IntegerField(default=0)
    package = models.IntegerField(null=True, blank=True)
    no_of_days = models.IntegerField(default=0)