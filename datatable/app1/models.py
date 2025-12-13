from django.db import models

# Create your models here.
class Car(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    colour=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
        
        