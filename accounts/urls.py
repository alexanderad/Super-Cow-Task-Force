# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import logout

urlpatterns = patterns('accounts.views',
    (r'^json/login', 'json_login'),
)