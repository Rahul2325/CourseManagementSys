from django.db import models

# Creating Model

class Course(models.Model):
    CourseName= models.CharField(max_length=50)
    CourseCredits= models.IntegerField(default=2)
    CourseImage=models.ImageField()
    Desc=models.TextField()
    Tags=models.CharField(max_length=50)