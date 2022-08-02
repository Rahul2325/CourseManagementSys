# from django.db import models
# from django.contrib.auth.models import User
# # # Create your models here.
# # # class Regform(models.Model):
# # #     # owner = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     firstName=models.CharField(max_length=30,unique=True)
# # #     lastName=models.CharField(max_length=30,unique=True)
# # #     username = models.CharField(max_length = 30,unique=True)
# # #     DOB= models.DateField()
# # #     email = models.CharField(max_length=30,unique=True)
# # #     password = models.CharField(max_length=30)
# # #     password2 = models.CharField(max_length=30)

    
# # #     def __str__(self):
# # #         return self.firstName 
# #         #  in admin panel, all of the above details will be store under the username
    
# class User(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.first_name