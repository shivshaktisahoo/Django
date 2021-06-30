from django.db import models

# Create your models here.

# default --> null = False, blank = False


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    desc = models.TextField()
    salary = models.FloatField()
    is_verify = models.BooleanField(default=False)

class Education(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    desc = models.TextField()
    salary = models.FloatField()
    is_verify = models.BooleanField(default=False)