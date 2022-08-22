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
    component = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    Modules = models.CharField(max_length=30)
    # Video=models.FileField(upload_to = "Video")

    def __str__(self):
        return self.Modules

class ModelUnits(models.Model):
    unit = models.ForeignKey(Components, on_delete=models.CASCADE, null=True)
    Units = models.CharField(max_length=30)
    Text = models.TextField()
    Video=models.TextField(max_length=100, null=True)
    def __str__(self):
        return self.Units

