# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

class QuickTestCheckForm(forms.Form):
    """ check form """
    url = forms.URLField(required=True, widget=forms.TextInput(attrs={"class": "link-input"}))

def quick_test(request):
    """ quick test page """
    return render_to_response('quick-test.html', {}, context_instance=RequestContext(request))

def index(request):
    """ index page """
    form = None
    if "POST" == request.method:
        form = QuickTestCheckForm(request.POST)
        if form.is_valid():
            assert False, "form is valid"            
    if form is None:
        form = QuickTestCheckForm()
    return render_to_response('index.html', {"form": form}, context_instance=RequestContext(request))