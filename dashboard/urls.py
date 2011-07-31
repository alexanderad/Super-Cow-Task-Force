# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('dashboard.views',
    (r'^settings', 'settings'),
    (r'^index', 'dashboard_index'),    
)