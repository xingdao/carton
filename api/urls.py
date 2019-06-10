#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author: qiao
"""
from django.conf.urls import url

# from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^app/$', views.AppList.as_view()),
    url(r'^app/(?P<uuid>\w{8}(-\w{4}){3}-\w{12})/$', views.AppDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
