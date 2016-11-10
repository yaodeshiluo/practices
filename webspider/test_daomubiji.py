import requests
from lxml import etree



def get_response(url):
    response = requests.get(url)
    return response

'''
def parse(response):




    sel = etree.HTML(response.text)
    tables = sel.xpath('//table')
    items = []
    for each in tables:

        links = each.xpath('tr/td/a/@href') #no tbody and not extract()
        contents = each.xpath('tr/td/a/text()') #no tbody and not extract()
        for i in range(len(links)):
            item = {}
            item['link'] = links[i]
            try:
                item['book'] = contents[i].split(' ')[0]
                item['chapter'] = contents[i].split(' ')[1]
            except Exception, e:
                continue

            try:
                item['name'] = contents[i].split(' ')[2]
            except Exception, e:
                item['name'] = contents[i].split(' ')[1][-3:]
            items.append(item)
    return items
'''

def parse(response):
    sel = etree.HTML(response.text)
    tables = sel.xpath('//table')
    items = []
    for each in tables:
        links = each.xpath('tr/td/a/@href')  # not tbody
        contents = each.xpath('tr/td/a/text()')  # not tbody
        for i in range(len(links)):
            item = {}
            item['link'] = links[i]
            try:
                item['book'] = contents[i].split(' ')[0]
                item['chapter'] = contents[i].split(' ')[1]
            except Exception, e:
                continue

            try:
                item['name'] = contents[i].split(' ')[2]
            except Exception, e:
                item['name'] = contents[i].split(' ')[1][-3:]
            items.append(item)
    return items


if __name__ == '__main__':
    url = 'http://www.daomubiji.com/'
    response = get_response(url)
    items = parse(response)
    print items