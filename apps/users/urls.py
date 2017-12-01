# _*_ coding: utf-8 _8
from django.conf.urls import url
from . import views
from .views import LogView

app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LogView.as_view(), name='login')
]
