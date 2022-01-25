from pyexpat import model
from traceback import print_exception
from turtle import title
from django.db import models

# Create your models here.

class Product(models.Model): ##inheritaed from model class
    title = models.CharField(max_length=255)
    desc = models.TextField()
    prce = models.DecimalField(max_digits=6 , decimal_places=2) # 9999.99
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)

class Customer(models.Model): ##inheritaed from model class
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField( unique=True) # 9999.99
    phone = models.CharField(max_length=255)
    birht_day = models.DateField(null=True)
