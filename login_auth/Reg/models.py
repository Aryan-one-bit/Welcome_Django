from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=30)
    Uname=models.CharField(max_length=30,primary_key=True)
    Password=models.CharField(max_length=30)