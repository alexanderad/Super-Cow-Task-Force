# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
import simplejson as json

class LoginForm(forms.Form):
    """ форма входа """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

def json_login(request):
    """ ajax json login """
    data = {}
    if "POST" == request.method:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {"error": 0, "valid": True}
        else:            
            data = {"error": 1, "form_errors": form.errors}
    return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype="application/json")