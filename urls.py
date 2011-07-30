# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    #(r'^index/', include('alice.core.urls')),
    (r'', 'index.views.welcome'),
)

# old school MEDIA
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(static)/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
