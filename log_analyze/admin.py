from django.contrib import admin
from .models import LogMonitor
from .models import UserLogSystem
from .models import UserLogWarning
from .models import UserLogError
from .models import UserLogInfo
from .models import LogLevel

# Register your models here.
# class LogMonitorAdmin(admin.ModelAdmin):
# 	pass
admin.site.register(LogMonitor)
admin.site.register(UserLogSystem)
admin.site.register(UserLogWarning)
admin.site.register(UserLogError)
admin.site.register(UserLogInfo)
admin.site.register(LogLevel)

admin.site.site_header = "Peanut Plan Admin"
admin.site.site_title = "Peanut Plan Admin"
