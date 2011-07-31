# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django import forms
from crawler.crawler import Crawler

class QuickTestCheckForm(forms.Form):
    """ check form """
    url = forms.URLField(required=True, widget=forms.TextInput(attrs={"class": "link-input"}))

def quick_test(request):
    """ quick test page """
    form, results, url_to_test = None, None, u''    
    if "POST" == request.method:
        form = QuickTestCheckForm(request.POST)
        if form.is_valid():
            url_to_test = form.cleaned_data["url"] 

    if "url-to-test" in request.session:
        url_to_test = request.session.pop("url-to-test")

    if url_to_test:
        # lets check
        c = Crawler(url_to_test)
        raw_results = c.run()
        results = {"error": raw_results["error"],
                   "results_by_category": ((u'External links', 'ext', raw_results["external"], len(raw_results["external"]["web"]) + len(raw_results["external"]["img"])),
                                           (u'Internal links', 'int', raw_results["internal"], len(raw_results["internal"]["web"]) + len(raw_results["internal"]["img"])),
                                           (u'System', 'system', raw_results["system"], len(raw_results["system"]["css"]) + len(raw_results["system"]["js"])),
            )
        }
    if form is None:
        initial = {}
        if url_to_test:
            initial.update({"url": url_to_test})
        form = QuickTestCheckForm(initial=initial)
    return render_to_response('index/quick-test.html', {"form": form, "results": results}, context_instance=RequestContext(request))

def index(request):
    """ index page """
    form = None
    if "POST" == request.method:
        form = QuickTestCheckForm(request.POST)
        if form.is_valid():
            # make love not war
            request.session["url-to-test"] = form.cleaned_data["url"]
            return HttpResponseRedirect(reverse('index.views.quick_test'))
    if form is None:
        form = QuickTestCheckForm()
    return render_to_response('index/index.html', {"form": form}, context_instance=RequestContext(request))

def how_it_works(request):
    """ how it works """
    return render_to_response('index/how-it-works.html', {}, context_instance=RequestContext(request))
