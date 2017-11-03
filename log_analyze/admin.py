from django.contrib import admin
from .models import LogMonitor
from .models import UserLogSystem
from .models import UserLogWarning
from .models import UserLogError
from .models import UserLogInfo
from .models import LogLevel
from .models import BizServiceError
from .models import AdminWebError
from .models import AlibblifeWebError
from .models import AlilifeServiceError
from .models import CommunicationServiceError
from .models import ConfigServiceError
from .models import MobileWebError
from .models import OrderServiceError
from .models import PayServiceError
from .models import PromotionServiceError
from .models import ShopServiceError
from .models import UserServiceError
from .models import WapWebError
from .models import WxServiceError

# Register your models here.
# class LogMonitorAdmin(admin.ModelAdmin):
# 	pass
admin.site.register(LogMonitor)
admin.site.register(UserLogSystem)
admin.site.register(UserLogWarning)
admin.site.register(UserLogError)
admin.site.register(UserLogInfo)
admin.site.register(LogLevel)
admin.site.register(BizServiceError)
admin.site.register(AdminWebError)
admin.site.register(AlibblifeWebError)
admin.site.register(AlilifeServiceError)
admin.site.register(CommunicationServiceError)
admin.site.register(ConfigServiceError)
admin.site.register(MobileWebError)
admin.site.register(OrderServiceError)
admin.site.register(PayServiceError)
admin.site.register(PromotionServiceError)
admin.site.register(ShopServiceError)
admin.site.register(UserServiceError)
admin.site.register(WapWebError)
admin.site.register(WxServiceError)

admin.site.site_header = "Peanut Plan Admin"
admin.site.site_title = "Peanut Plan Admin"


