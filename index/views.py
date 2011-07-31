# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response

def quick_test(request):
    """ quick test page """
    return render_to_response('quick-test.html', {}, context_instance=RequestContext(request))

def index(request):
    """ index page """
    return render_to_response('index.html', {}, context_instance=RequestContext(request))