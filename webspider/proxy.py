import urllib
import urllib2
import re

def get_html(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36' )
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
    print html
    return html

def get_proxy(html):
    pattern = re.compile(r'(?:(?:[0,1]?[0-9][0-9]|[0-9]|[2][0-4][0-9]|25[0-5])\.){3}(?:[0,1]?[0-9][0-9]|[0-9]|[2][0-4][0-9]|25[0-5])')
    proxy_list = re.findall(pattern,html)
    for i in proxy_list:
        print i

def start():
    url = 'http://www.proxy360.cn/'
    html = get_html(url)
    print html
    get_proxy(html)

if __name__ == '__main__':
    start()


