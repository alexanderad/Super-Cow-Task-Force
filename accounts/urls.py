# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
    (r'^logout', 'logout'),
    (r'^json/login', 'json_login'),
    (r'^json/register', 'json_register'),
)