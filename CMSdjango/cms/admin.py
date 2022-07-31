from django.contrib import admin
from cms.models import Userlist

class UserDisplay(admin.ModelAdmin):
    list_display=('id','firstName', 'email',)
    list_display_links=('firstName',)
    list_filter=('firstName',)



# Register your models here.
# admin.site.register(Regform)
admin.site.register(Userlist,UserDisplay)