from django.shortcuts import render
# from .forms import LogMonitorForm

# Create your views here.
def index(request):
	# if request.method=='POST':#when commit form
	# 	form = LogMonitorForm(request.POST)#Data in Form
	# 	if form.is_valid():
	# 		pass
	# else:
	# 	form = LogMonitorForm()
	return render(request,'log_analyze/index.html')