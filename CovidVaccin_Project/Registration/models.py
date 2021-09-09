from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Vaccine_Center(models.Model):
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    Created_by = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    First_Name = models.CharField(max_length=250)
    Last_name = models.CharField(max_length=40)
    Email = models.CharField(max_length=250)
    Address = models.CharField(max_length=350)
    Contact_Number = models.CharField(max_length=10)
    Age = models.IntegerField()
    district = models.ForeignKey(District,on_delete=models.SET_NULL, blank=True, null=True)
    vaccine_center = models.ForeignKey(Vaccine_Center,on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.First_Name

