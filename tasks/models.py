# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tasks.constants import LINK_TYPES

class Task(models.Model):
    """ Model for tasks """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128, default=u'')
    def __unicode__(self):
        return self.name

class Page(models.Model):
    """ Model for Pages in Task """
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=128, default=u'')
    url = models.URLField(verify_exists=False, max_length=2048)    
    @property
    def get_stats(self):
        #TODO
        return {}
        
class Link(models.Model):
    """ Model for Link on a Page """
    page = models.ForeignKey(Page)
    link = models.CharField(max_length=2048, default=u'')
    link_type = models.CharField(max_length=8, choices=LINK_TYPES, default='web')
    link_anchor = models.CharField(max_length=256, default=u'')
    remote_page_title = models.CharField(max_length=256, default=u'')
    img_size = models.IntegerField(default=0)
    def __unicode__(self):
        return self.link if len(self.link) < 32 else u'%s...' % self.link[:32]    
