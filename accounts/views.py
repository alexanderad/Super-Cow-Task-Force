# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
import simplejson as json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.core.urlresolvers import reverse

class LoginForm(forms.Form):
    """ login form """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class RegistrationForm(forms.Form):
    """ registration form """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    password_verification = forms.CharField(required=True)    

def json_register(request):
    """ ajax json register """
    data = {}
    if "POST" == request.method:
        form = RegistrationForm(request.POST)
        if form.is_valid():            
            if form.cleaned_data["password"] != form.cleaned_data["password_verification"]:
                data = {"error": 2, "non_field_error": "Passwords do not match."}
            elif User.objects.filter(username=form.cleaned_data["email"]).count() > 0:
                data = {"error": 3, "non_field_error": "Account already exists."}
            else:
                # everything is ok
                u = User.objects.create_user(form.cleaned_data["email"], form.cleaned_data["email"], form.cleaned_data["password"])
                UserProfile.objects.create(user=u)
                # authenticate immediately
                u = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password"])
                login(request, u)
                data = {"error": 0}
        else:            
            data = {"error": 1, "form_errors": form.errors}
    return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype="application/json")

def json_login(request):
    """ ajax json login """
    data = {}
    if "POST" == request.method:
        form = LoginForm(request.POST)
        if form.is_valid():            
            u = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if u is not None and u.is_active:
                login(request, u)
                data = {"error": 0}
            else:
                data = {"error": 403, "non_field_error": "Invalid username and/or password."}
        else:            
            data = {"error": 1, "form_errors": form.errors}
    return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype="application/json")
    
def account_logout(request):
    """ logout """
    logout(request)    
    return HttpResponseRedirect(reverse('index.views.index'))