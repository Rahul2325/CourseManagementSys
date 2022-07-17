from django.db import models
# Create your models here.
class Regform(models.Model):
    firstName=models.CharField(max_length=30,unique=True)
    lastName=models.CharField(max_length=30,unique=True)
    username = models.CharField(max_length = 30,unique=True)
    DOB= models.DateField()
    email = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30,unique=True)

    
    def _str_(self):
        return self.username
    