from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Regform(models.Model):
#     # owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     firstName=models.CharField(max_length=30,unique=True)
#     lastName=models.CharField(max_length=30,unique=True)
#     username = models.CharField(max_length = 30,unique=True)
#     DOB= models.DateField()
#     email = models.CharField(max_length=30,unique=True)
#     password = models.CharField(max_length=30)
#     password2 = models.CharField(max_length=30)

    
#     def __str__(self):
#         return self.firstName 
        #  in admin panel, all of the above details will be store under the username
    
class Userlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=30,unique=True, default='Some string')
    lastName=models.CharField(max_length=30,unique=True, default='Some string')
    username = models.CharField(max_length = 30,unique=True, default='Some string')
    DOB= models.DateField()
    email = models.CharField(max_length=30,unique=True, default='Some string')
    password = models.CharField(max_length=30, default='Some string')
    password2 = models.CharField(max_length=30, default='Some string')

    def __str__(self):
        return self.firstName