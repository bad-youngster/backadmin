# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from cmdb.devicetype import views
from cmdb.excel import views as excel

app_name = "cmdb"

urlpatterns = [
    url(r'^$',views.cmdb,name="cmdbindex"),
    url(r'^devicestatus/$',views.insert,name="devicestatus"),
    url(r'^devicelist/$',views.list,name="devicelist"),
    url(r'^new/$',views.new,name="new"),
    url(r'^export_excel/$', excel.export_xls, name="export_xls"),

]