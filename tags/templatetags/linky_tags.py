# -*- coding: utf-8 -*-
from django import template
from tasks.constants import LINK_TYPES_DICT

register = template.Library()

@register.filter
def link_type_display(link_type):
    """ link type display """
    return LINK_TYPES_DICT.get(link_type)
    
@register.filter
def get_link_status_icon(l):
    if l["http_status"] == 200:
        return 'ok'
    return 'warning'
    