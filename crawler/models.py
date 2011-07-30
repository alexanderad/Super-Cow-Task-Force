# -*- coding: utf-8 -*-
from django.db import models
from tasks.models import Link
from tasks.constants import LINK_STATUSES

class CrawlerRecord(models.Model):
    """ Crawler visit record for Link """
    link = models.ForeignKey(Link)
    visited_at = models.DateTimeField()
    http_status = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=32, choices=LINK_STATUSES)
    def __unicode__(self):
        return u'HTTP %d: %s' % (self.status, self.get_status_display)
