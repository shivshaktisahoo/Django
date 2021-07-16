from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    contactno = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='customer/photo/', null=True, blank=True)