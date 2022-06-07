from django.contrib import admin
from . models import *
# Register your models here.
class eventadmin(admin.ModelAdmin):
    list_display = ['event_name','event_coordinator','register_link']

admin.site.register(events,eventadmin)

admin.site.register(shows)

admin.site.register(gallery)