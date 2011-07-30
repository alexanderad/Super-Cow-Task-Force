# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response

def welcome(request):
    """ index page """
    return render_to_response('welcome.html', {}, context_instance=RequestContext(request))