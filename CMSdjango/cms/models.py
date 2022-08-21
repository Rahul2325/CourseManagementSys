from django.db import models

# Creating Model

class Course(models.Model):
    CourseName= models.CharField(max_length=50)
    CourseCredits= models.IntegerField(default=0)
    CourseImage=models.ImageField(upload_to = "media")
    Desc=models.TextField()
    Tags=models.CharField(max_length=50)

    def __str__(self):
        return self.CourseName

class Components(models.Model):
    Modules=models.CharField(max_length=30)
    Units=models.CharField(max_length=30)
    Text=models.TextField()
    # Video=models.FileField(upload_to = "Video")

    def __str__(self):
        return self.Modules
