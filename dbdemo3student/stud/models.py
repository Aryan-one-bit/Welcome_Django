from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=15)
    sub1=models.FloatField()
    sub2=models.FloatField()
    