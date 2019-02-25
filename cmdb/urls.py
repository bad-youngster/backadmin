# -*- coding: utf-8 -*-
from django.conf.urls import url

from cmdb.devicetype import views
from cmdb.excel.export_excel import views as excel
from cmdb.excel.upload_excel import views as upload

app_name = "cmdb"

urlpatterns = [
    url(r'^$',views.cmdb,name="cmdbindex"),
    url(r'^devicestatus/$',views.insert,name="devicestatus"),
    url(r'^devicelist/$',views.list,name="devicelist"),
    url(r'^new/$',views.new,name="new"),
    url(r'^export_excel/$', excel.export_xls, name="export_xls"),
    url(r'^upload_excel/$',upload.excel_upload,name="excel_upload"),

]