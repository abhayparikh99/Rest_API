from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    city = models.CharField(max_length=30,default="Ahmedabad")