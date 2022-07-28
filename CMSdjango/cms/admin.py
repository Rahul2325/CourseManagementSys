from django.contrib import admin
from cms.models import Regform

class RegformUser(admin.ModelAdmin):
    list_display=('id','firstName', 'email')
    list_display_links=('firstName' ,)
    list_filter=('email' ,)

# Register your models here.
admin.site.register(Regform, RegformUser)