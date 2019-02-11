from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.login_page, name="login"),
    url(r'checkcode', views.getcheck_code),
    url(r'welcome', views.welcome),
]
