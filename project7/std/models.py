from django.db import models

# Create your models here.


class StudentRegister(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    submitted_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    