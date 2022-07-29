from django.contrib import admin
from cms.models import Userlist

class RegformUser(admin.ModelAdmin):
    list_display=('firstName', 'email',)
    list_display_links=('firstName',)
    list_filter=('firstName',)



# Register your models here.
# admin.site.register(Regform)
admin.site.register(Userlist, RegformUser)