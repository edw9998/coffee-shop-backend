from xmlrpc.client import ResponseError
from django.db import models

# Create your models here.
class Item(models.Model):
    HTTP_Method = models.CharField(max_length=1000)
    URL_Endpoint = models.CharField(max_length=1000)
    Request_Body = models.Charfield(max_length=1000)
    Response_Body = models.Charfield(max_length=1000)
    Created_At = models.DateTimeField(auto_now_add=True)
