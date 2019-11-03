from django.contrib import admin
from accounts.models import User
from accounts.forms import usercreationform,userchangeform


class customadmin(admin.ModelAdmin):
    search_fields=['email']
    list_display=("email","first_name","last_name","time_stamp","admin")
    list_filter=("admin","staff","active")
    form=userchangeform
    add_form=usercreationform


admin.site.register(User, customadmin)
