#for log_analyze's urls

from django.conf.urls import url
from django.contrib import admin
from log_analyze import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^biz_service_error/$',views.biz_service_error,name='bizerror'),
    #url(r'^alibblife_web_error/$',views.biz_service_error,name='alibblifeerror'),
    url(r'^admin_web_error/$',views.admin_web_error,name='adminerror'),
    url(r'^alilife_service_error/$',views.alilife_service_error,name='alilifeerror'),
    url(r'^commun_service_error/$',views.commun_service_error,name='communerror'),
    url(r'^config_service_error/$',views.config_service_error,name='configerror'),
    url(r'^mobile_web_error/$',views.mobile_web_error,name='mobileerror'),
    url(r'^order_service_error/$',views.order_service_error,name='ordererror'),
    url(r'^promotion_service_error/$',views.promotion_service_error,name='promotionerror'),
    url(r'^wap_service_error/$',views.wap_service_error,name='waperror'),
    url(r'^wx_service_error/$',views.wx_service_error,name='wxerror'),
    url(r'^user_service_error/$',views.user_service_error,name='usererror'),
    url(r'^pay_service_error/$',views.pay_service_error,name='payerror'),
    url(r'^shop_service_error/$',views.shop_service_error,name='shoperror'),
    url(r'^test_host/$',views.test_host,name='test'),
    url(r'^remote_host/$',views.remote_host,name='remote'),
    url(r'^biz_host/$',views.biz_host,name='bizhost'),
    url(r'^host_94/$',views.host_94,name='host94'),
    url(r'^host_98/$',views.host_98,name='host98'),
    url(r'^remote_biz_info_94/$',views.remote_biz_info_94,name='remotebizinfo94'),
    url(r'^remote_biz_error_94/$',views.remote_biz_error_94,name='remotebizerror94'),
    url(r'^remote_biz_info_98/$',views.remote_biz_info_98,name='remotebizinfo98'),
    url(r'^remote_biz_error_98/$',views.remote_biz_error_98,name='remotebizerror98'),
]
