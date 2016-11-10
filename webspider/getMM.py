#encoding:utf-8
import re
import urllib
import urllib2
import os
import random

def opener(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
    proxy = '122.72.18.160:80'
    proxy_support = urllib2.ProxyHandler({'http':proxy})
    new_opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(new_opener)
    response = urllib2.urlopen(request)
    return response.read()


def first_page():
    pattern = re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    html = opener('http://jandan.net/ooxx')
    p = re.findall(pattern,html.decode('utf-8'))[0]
    print p
    return p


def get_url(i):
    baseurl = 'http://jandan.net/ooxx'
    page0 = first_page()
    s = int(page0) - i
    url = baseurl + '/page-%s#comments'% s
    return url

def get_html(url):
    html = opener(url)
    return html.decode('utf-8')

def get_links(html):
    pattern = re.compile(r'<a href="([^"]+\.jpg)"',re.S)
    links = re.findall(pattern,html)
    return links


def download_mm(num):
    os.mkdir('MMpictures')
    os.chdir('MMpictures')



    for i in range(num):
        url = get_url(i)
        html = get_html(url)
        links = get_links(html)
        print links
        for link in links:
            img = opener(link)
            filename = link.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(img)



if __name__ == '__main__':
    download_mm(10)
