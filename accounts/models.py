# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from accounts.constants import NOTIFICATIONS_SETTINGS
from crawler.constants import CRAWLER_VISITS_FREQ

class UserProfile(models.Model):
    """ User profile """
    user = models.OneToOneField(User, unique=True)
    # user preferences (scan defaults for newly created Task)
    notifications_settings = models.CharField(max_length=32, choices=NOTIFICATIONS_SETTINGS, default='dashboard-only')
    crawler_visits_frequency = models.CharField(max_length=16, choices=CRAWLER_VISITS_FREQ, default='daily')
    limit_link_types = models.CharField(max_length=32, default=u'web css js img') # space separated link types
    def __unicode__(self):
        return u'Profile for %s' % self
