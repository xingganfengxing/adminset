#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='monitor'),
    url(r'^host/info/(?P<hostname>\w+)/$', views.host_info, name='host_info'),
    url(r'^get/data/(?P<hostname>\w+)/$', views.get_sys_data, name='get_sys_data'),
]