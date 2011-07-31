# -*- coding: utf-8 -*-
import re
import urllib2
import socket
from BeautifulSoup import BeautifulSoup as Soup
from threading import Thread
from Queue import Queue
from tasks.constants import LINK_TYPES_DICT
from BaseHTTPServer import BaseHTTPRequestHandler
from django.utils.html import strip_tags, strip_entities

# set timeout
socket.setdefaulttimeout(5)

HTTP_RESPONSE_CODES = BaseHTTPRequestHandler.responses

SOUP_NAMES2LINK_TYPES = {'link': 'css',
                         'a': 'web',
                         'img': 'img',
                         'script': 'js'}

class HEADRequest(urllib2.Request):
    """ HEAD request """
    def get_method(self):
        return "HEAD"

def get_link_target(host, link):
    """ figure out if link is internal or external """
    link_host = get_host(link)    
    return 'internal' if not link_host or link_host == host else 'external' 

def get_host(link):
    """ return host of link if possible """
    match = re.search(r'//(?P<host>[A-Z-a-z\.]+)/', link)
    if match:
        return match.group('host')
    return None

def perform_head_request(url):
    """ perform HEAD request """    
    try:
        response = urllib2.urlopen(HEADRequest(url))
        return {"http_status": response.getcode(), 
                "size": response.headers["Content-Length"] if response.headers.has_key("Content-Length") else 0}
    except urllib2.HTTPError, e:
        return {"http_status": getattr(e, "code", -1), "verbose": u'%s' % e}            
    except Exception, e:
        return {"http_status": -1, "verbose": u'%s' % e}        

#def perform_get_request(url):
    #""" try to get <title></title> contents of url """
    #return {}
    #try:
        #response = urllib2.urlopen(url)        
        #title = Soup(response.read(1024)).find('title')
        #return {"http_status": response.getcode(),
                #"title": title.text if title else u''}
    #except urllib2.URLError, e:
        ##return {"http_status": 404}
        #pass
    #return {}        

def get_link_type(soup_name):
    """ convert soup name to linky link type """
    return SOUP_NAMES2LINK_TYPES.get(soup_name)

def get_anchor(soup_element, link):
    # web
    if soup_element.text:
        return soup_element.text
    # images
    for k in ["title", "alt"]:
        if soup_element.has_key(k) and soup_element[k]:
            return soup_element[k]
    # css/js & other 
    try:
        return link.split("/")[-1]
    except IndexError:
        pass
    return u''

#FIXME
def get_full_link(host, link):
    """ get full link """
    if not link.startswith("http://") and not link.startswith("https://"):
         return u'http://%s%s' % (host, '/' + link if not link.startswith("/") else link)
    return link

class Crawler:
    """ Page crawler """
    def __init__(self, page_url, link_types=None):
        self.url = page_url
        self.link_types = link_types or 'web css js img' #TODO
        self.results = {'error': 0, 'external': {'web': [], 
                                                 'img': []}, 
                                    'internal': {'web': [], 
                                                 'img': []},
                                    'system': {'css': [],
                                               'js': []},
        }
        self.q = Queue(50)

    def worker(self):
        while True:
            l = self.q.get()
            self.check_link(l)
            self.q.task_done() 

    def check_link(self, data):
        """ check link """
        data.update(perform_head_request(data["full_link"]))
        if data["link_type"] in ["web", "img"]:
            self.results[data["link_target"]][data["link_type"]].append(data)
        else:
            self.results["system"][data["link_type"]].append(data)

    def run(self):
        """ get page """        
        request = urllib2.Request(self.url)
        try:
            response = urllib2.urlopen(request)
            page_data = response.read()
        except Exception, e:
            results = {'error': -1, 'exception': e}
            return results

        http_status = response.getcode()
        if http_status in [200]:
            # run threads
            for i in range(0, 15):
                t = Thread(target=self.worker)
                t.daemon = True
                t.start()

            self.host = request.host
            all_links = Soup(page_data).findAll(['a', 'img', 'script', 'link'])
            all_links_filtered = []
            for l in all_links:
                link = None
                if l.name in ['a', 'link'] and l.has_key('href'):
                    link = l["href"].strip()
                    #TODO: favicons, rss/atom feeds, etc 
                    if 'link' == l.name and (not l.has_key("type") or l["type"] != "text/css"):
                        continue
                if l.name in ['img', 'script'] and l.has_key('src'):
                    link = l["src"].strip()
                if link and link not in all_links_filtered:

                    #HACK
                    if link.startswith("//"):
                        link = u'http:' + link

                    self.q.put({"link_target": get_link_target(self.host, link),
                                "link_type": get_link_type(l.name),                                
                                "full_link": get_full_link(self.host, link),
                                "link_anchor": strip_tags(strip_entities(get_anchor(l, link))),
                                "link": link,
                    })
                    all_links_filtered.append(link)
            self.q.join()           
        else:
            self.results = {'error': response.code}
        return self.results