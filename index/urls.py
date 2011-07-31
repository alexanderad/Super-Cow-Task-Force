# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('index.views',
    (r'^quick-test', 'quick_test'),
    (r'^how-it-works', 'how_it_works'),
)