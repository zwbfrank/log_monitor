#for log_analyze's urls

from django.conf.urls import url
from django.contrib import admin
from log_analyze import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^biz_service_error/$',views.biz_service_error,name='bizerror'),
    url(r'^alibblife_web_error/$',views.biz_service_error,name='alibblifeerror'),
    url(r'^admin_web_error/$',views.biz_service_error,name='adminerror'),
    url(r'^alilife_service_error/$',views.biz_service_error,name='alilifeerror'),
    url(r'^commun_service_error/$',views.biz_service_error,name='communerror'),
    url(r'^config_service_error/$',views.biz_service_error,name='configerror'),
    url(r'^mobile_web_error/$',views.biz_service_error,name='mobileerror'),
    url(r'^order_service_error/$',views.biz_service_error,name='ordererror'),
    url(r'^promotion_service_error/$',views.biz_service_error,name='promotionerror'),
    url(r'^wap_service_error/$',views.biz_service_error,name='waperror'),
    url(r'^wx_service_error/$',views.biz_service_error,name='wxerror'),
    url(r'^user_service_error/$',views.biz_service_error,name='usererror'),
    url(r'^pay_service_error/$',views.biz_service_error,name='payerror'),
    url(r'^shop_service_error/$',views.biz_service_error,name='shoperror'),
]
