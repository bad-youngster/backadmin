from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'table', views.table, name='table'),
    url(r'test', views.test, name='table'),
    url(r'appadmin/', include("appadmin.urls")),
    # url(r'',include())
]
