# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def settings(request):
    """ settings page """
    #TODO: create form & save settings into profile fields
    return render_to_response('dashboard/settings.html', {}, context_instance=RequestContext(request))

@login_required(login_url='/')
def dashboard_index(request):
    """ dashboard index page """
    #TODO
    return render_to_response('dashboard/dashboard-index.html', {}, context_instance=RequestContext(request))
