from django.contrib import admin
from cms.models import Userlist

class RegformUser(admin.ModelAdmin):
    list_display=('first_name', 'email',)
    list_display_links=('first_name',)
    # list_filter=('firstName',)



# Register your models here.
# admin.site.register(Regform)
admin.site.register(Userlist)