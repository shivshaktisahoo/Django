from django.db import models

# no mandatory stuff put - True(by default its False)
# null=False, blank=False
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    desc = models.TextField()
    is_verify = models.BooleanField(default=False) # if user doesnot mention anything by default it will take False