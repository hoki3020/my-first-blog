# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:40:37 2019

@author: hoki
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]