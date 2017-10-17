from django.contrib import admin
from .models import LogMonitor
from .models import UserLog

# Register your models here.
# class LogMonitorAdmin(admin.ModelAdmin):
# 	pass
admin.site.register(LogMonitor)
admin.site.register(UserLog)
admin.site.site_header = "Peanut Plan Admin"
admin.site.site_title = "Peanut Plan Admin"
