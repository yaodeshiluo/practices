#encoding:utf-8
import requests
from lxml import etree
from multiprocessing.dummy import Pool
import json
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

def get_url(pages):
    url_list = []
    for each in range(pages+1):
        url = 'http://tieba.baidu.com/p/3920618845?pn=' + str(each)
        url_list.append(url)
    return url_list

def towrite(author,reply_time,content):
    f.writelines(author.encode('utf-8') + '\n')
    f.writelines(reply_time.encode('utf-8') + '\n')
    f.writelines(content.encode('utf-8') + '\n\n')


def spider(url):
    html = requests.get(url).text
    selector = etree.HTML(html)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    print content_field,type(content_field)
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0])
        print reply_info
        author = reply_info['author']["user_name"]
        reply_time = reply_info['content']['date']
        forcontent = each.xpath('div[@class="d_post_content_main"]//div//cc//div')[0]
        content = forcontent.xpath('string(.)')
        towrite(author, reply_time, content)

if __name__ == '__main__':
    filename = u'大鱼海棠贴吧评论.txt'
    f = open(filename,'a')
    url_list = get_url(10)
    pool = Pool(4)
    pool.map(spider,url_list)
    pool.close()
    pool.join()
    f.close()






