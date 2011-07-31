# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django import forms

def settings(request):
    """ settings page """
    return render_to_response('dashboard/settings.html', {}, context_instance=RequestContext(request))

def dashboard_index(request):
    """ dashboard index page """
    return render_to_response('dashboard/dashboard-index.html', {}, context_instance=RequestContext(request))
