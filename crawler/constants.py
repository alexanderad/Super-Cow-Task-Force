# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler

HTTP_RESPONSE_CODES = BaseHTTPRequestHandler.responses

CRAWLER_VISITS_FREQ = (
                       ('hourly', u'Every hour'),
                       ('daily', u'Daily'),
                       ('weekly', u'Weekly'),
                       ('twice-a-week', u'Twice a week'),
)

