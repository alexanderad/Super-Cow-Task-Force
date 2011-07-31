# -*- coding: utf-8 -*-
import re
import urllib2
from BeautifulSoup import BeautifulSoup as Soup
#from crawler.constants import HTTP_RESPONSE_CODES
from BaseHTTPServer import BaseHTTPRequestHandler


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
    except urllib2.URLError, e:
        pass
    return {}

def perform_get_request(url):
    """ try to get <title></title> contents of url """
    try:
        response = urllib2.urlopen(url)        
        title = Soup(response.read(1024)).find('title')
        return {"http_status": response.getcode(),
                "title": title.text if title else u''}
    except urllib2.URLError, e:
        pass
    return {}        

def get_link_type(soup_name):
    """ convert soup name to linky link type """
    return SOUP_NAMES2LINK_TYPES.get(soup_name)

#FIXME
def get_full_link(host, link):
    """ get full link """
    if not link.startswith("http://") and not link.startswith("https://"):
         return u'http://%s%s' % (host, '/' + link if not link.startswith("/") else link)
    return link

def check_link(host, soup_element, link):
    """ check link """
    full_link = get_full_link(host, link)
    data = {"link": link, "full_link": full_link}
    if 'a' == soup_element.name:
        data.update(perform_get_request(full_link))
        data.update({"link_anchor": soup_element.text})
    else:
        data.update(perform_head_request(full_link))
    print data
    return data

class Crawler:
    """ Page crawler """
    def __init__(self, page_url, link_types=None, task_instance=None):
        self.url = page_url
        self.link_types = link_types or 'web css js img'
        self.task = task_instance

    def parse(self):
        """ get page """
        results = {'error': 0, 'internal': {}, 'external': {}}
        request = urllib2.Request(self.url)
        try:
            response = urllib2.urlopen(request)
            page_data = response.read()
        except urllib2.URLError, e:
            results = {'error': -1, 'exception': e}
            return results

        http_status = response.getcode()
        if http_status in [200]:
            host = request.host
            checked_links = []
            for l in Soup(page_data).findAll(['a', 'img', 'script', 'link']):
                # find all links on a page
                link = None
                if l.name in ['a', 'link'] and l.has_key('href'):
                    link = l["href"].strip()
                if l.name in ['img', 'script'] and l.has_key('src'):
                    link = l["src"].strip()
                if link and link not in checked_links:
                    # external or internal?
                    link_target = get_link_target(host, link)
                    link_type = get_link_type(l.name)
                    if not results[link_target].has_key(link_type):
                        results[link_target].update({link_type: []})
                    results[link_target][link_type].append(check_link(host, l, link))
                    checked_links.append(link)
        else:
            results = {'error': response.code}
        return results

    def run(self):
        """ run crawler """
        from pprint import pprint
        pprint(self.parse()) 


c = Crawler('http://darednaxella.livejournal.com') 
c.run()
