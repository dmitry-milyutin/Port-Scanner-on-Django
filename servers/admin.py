from django.contrib import admin
from .models import *

admin.site.register(Port)
admin.site.register(ScannedPorts)


class ScannedPortsAdmin(admin.ModelAdmin):
    list_display = ('ip', 'ports', 'scanned_at') 


# Register your models here.
