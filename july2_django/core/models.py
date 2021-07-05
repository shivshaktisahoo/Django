from django.db import models

# Create your models here.

class Contactinfo(models.Model): 
    firstname = models.CharField(max_length=40,default="")
    lastname = models.CharField(max_length=20,default="")
    description = models.CharField(max_length=200,default="")
    