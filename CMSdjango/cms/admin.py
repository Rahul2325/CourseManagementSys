from django.contrib import admin
from cms.models import Userlist

class RegformUser(admin.ModelAdmin):
    list_display=('id', 'DOB',)
    list_display_links=('id',)
    list_filter=('id',)



# Register your models here.
# admin.site.register(Regform)
admin.site.register(Userlist, RegformUser)