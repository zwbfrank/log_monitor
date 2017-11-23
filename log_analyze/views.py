from django.shortcuts import render
from .models import BizServiceError
# from .models import AlibblifeWebError
from .models import AdminWebError
from .models import AlilifeServiceError
from .models import CommunicationServiceError
from .models import ConfigServiceError
from .models import MobileWebError
from .models import OrderServiceError
from .models import PayServiceError
from .models import PromotionServiceError
from .models import ShopServiceError
from .models import WapWebError
from .models import WxServiceError
from .models import UserServiceError
from .models import RemoteBizInfo94
from .models import RemoteBizError94
from .models import RemoteBizInfo98
from .models import RemoteBizError98
# from .forms import LogMonitorForm

# Create your views here.
def index(request):
    return render(request,'log_analyze/index.html')

def test_host(request):
    return render(request,'log_analyze/test.html')

def remote_host(request):
    return render(request,'log_analyze/remote.html')

def biz_host(request):
    return render(request,'log_analyze/biz_host.html')

def host_94(request):
    return render(request,'log_analyze/host_94.html')

def host_98(request):
    return render(request,'log_analyze/host_98.html')

def remote_biz_info_94(request):
    logs = RemoteBizInfo94.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/remote_biz_info_94.html',context)

def remote_biz_error_94(request):
    logs = RemoteBizError94.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/remote_biz_error_94.html',context)

def remote_biz_info_98(request):
    logs = RemoteBizInfo98.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/remote_biz_info_98.html',context)

def remote_biz_error_98(request):
    logs = RemoteBizError98.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/remote_biz_error_98.html',context)

def biz_service_error(request):
    logs = BizServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs} 
    return render(request,'log_analyze/bizerror.html',context)

# def alibblife_web_error(request):
#     logs = AlibblifeWebError.objects.all()
#     logs = reversed(logs)
#     context = {'logs':logs}
#     return render(request,'log_analyze/alibblifeerror.html',context)

def admin_web_error(request):
    logs = AdminWebError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/adminerror.html',context)

def alilife_service_error(request):
    logs = AlilifeServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/alilifeerror.html',context)

def commun_service_error(request):
    logs = CommunicationServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/communerror.html',context)

def config_service_error(request):
    logs = ConfigServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/configerror.html',context)

def mobile_web_error(request):
    logs = MobileWebError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/mobileerror.html',context)

def order_service_error(request):
    logs = OrderServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/ordererror.html',context)

def pay_service_error(request):
    logs = PayServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/payerror.html',context)

def promotion_service_error(request):
    logs = PromotionServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/promotionerror.html',context)

def shop_service_error(request):
    logs = ShopServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/shoperror.html',context)

def wap_service_error(request):
    logs = WapWebError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/waperror.html',context)

def wx_service_error(request):
    logs = WxServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/wxerror.html',context)

def user_service_error(request):
    logs = UserServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/usererror.html',context)

