# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    #(r'^dashboard/', include('dashboard.urls')),
    (r'^accounts/', include('accounts.urls')),
    #(r'^tasks/', include('tasks.urls')),    
    (r'^index/quick-test', 'index.views.quick_test'),
    (r'^$', 'index.views.index'),
)

# old school MEDIA
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(static)/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
