from django.contrib import admin

from cms.models import Course
# from cms.models import User

class CourseDisplay(admin.ModelAdmin):
    list_display=('id','CourseName', 'Desc','CourseImage',)
    list_display_links=('CourseName',)
    list_filter=('CourseName',)


admin.site.register(Course,CourseDisplay)





# Register your models here.
# admin.site.register(Regform)
# admin.site.register(User)