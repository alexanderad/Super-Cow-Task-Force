# -*- coding: utf-8 -*-
LINK_TYPES = (
                ('css', u'CSS'),
                ('js', u'JavaScript'),
                ('img', u'Images'),
                ('web', u'Web Pages'), 
)

LINK_TYPES_DICT = dict(LINK_TYPES)

LINK_STATUSES = (
                ('ok', u'Ok'),
                ('temporary-unavailable', u'Temporary unavailable'),
                ('muted', u'Muted'),
                ('dead', 'Dead'),
)

STATUS2ICON = {404: 'error',
               403: 'warning',
               200: 'ok',
               500: 'error',
               -1: 'error',
}


LINK_STATUSES_DICT = dict(LINK_STATUSES)