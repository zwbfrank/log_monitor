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