from xmlrpc.client import ResponseError
from django.db import models

# Create your models here.
class Item(models.Model):
    Name = models.CharField(max_length=1000)
    E-mail= models.CharField(max_length=1000)
    Password = models.Charfield(max_length=1000)
    Created = models.DateTimeField(auto_now_add=True)
