from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'index/$', views.index, name='index'),
    url(r'^table/', views.table, name='table'),
    url(r'^test/', views.test, name='test'),
    url(r'appadmin/', include("appadmin.urls")),
    url(r'^cmdb/',include('cmdb.urls')),
    url(r'api-auth/',include('rest_framework.urls',namespace='rest_framework'))
    # url(r'',include())
]
