from django.shortcuts import render
from .models import BizServiceError
# from .forms import LogMonitorForm

# Create your views here.
def index(request):

    return render(request,'log_analyze/index.html')

def biz_service_error(request):
    logs = BizServiceError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/bizerror.html',context)

def alibblife_web_error(request):
    logs = AlibblifeWebError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/alibblifeerror.html',context)

def admin_web_error(request):
    logs = AdminWebError.objects.all()
    logs = reversed(logs)
    context = {'logs':logs}
    return render(request,'log_analyze/adminerror.html',context)

def alilife_service_error(request):
    logs = BizServiceError.objects.all()
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

