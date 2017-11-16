#for log_analyze's urls

from django.conf.urls import url
from django.contrib import admin
from log_analyze import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^biz_service_error/$',views.biz_service_error,name='bizerror'),
]