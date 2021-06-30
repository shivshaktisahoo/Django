from django.db import models

# Create your models here.
class Education(models.Model):
    first_name = models.CharField(max_length=50, default="", editable=False)
    last_name = models.CharField(max_length=50, default="", editable=False)
    school = models.CharField(max_length=40, default="", editable=False)
    school_certificate = models.FileField(null=True, blank=True)
    highschool = models.CharField(max_length=40, default="", editable=False)
    highschool_certificate = models.FileField(null=True, blank=True)
    college = models.CharField(max_length=40, default="", editable=False)
    college_certificate = models.FileField(null=True, blank=True)

class Designation(models.Model):
    firstname = models.CharField(max_length=50, default="", editable=False)
    lastname = models.CharField(max_length=50, default="", editable=False)
    photo = models.FileField(null=True, blank=True)
    dateofjoining = models.DateField(null=True, blank=True)
    employee_id = models.IntegerField(null=True, blank=True)
    desg_name = models.CharField(max_length=20, default="", editable=False)
    company = models.CharField(max_length=20, default="", editable=False)
    role = models.CharField(max_length=20, default="", editable=False)
 