import re
re.match(r'^\\\d{3}\-\d{3,8}$', '\\010-12345')

re.split(r'[\s,;]+', 'a,b;; c  d')

m=re.match(r'(\d{3})-(\d{5})','010-12345')
m.group(2)
re.match(r'[pP]ython','python')

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()

re.match(r'<img.*?>|       ','       ')


#关于编码问题
import urllib
import urllib2
import re

baseUrl = 'https://mm.taobao.com/json/request_top_list.htm'
url = baseUrl + '?page=' + str(1)
request = urllib2.Request(url)
respond = urllib2.urlopen(request)
print type(respond.read())
page = respond.read().decode('GBK')
print page



import json
s = "{&quot;author&quot;:{&quot;user_id&quot;:147544700,&quot;user_name&quot;:&quot;\u51b7\u5cf0\u6b8b\u96ea&quot;,&quot;name_u&quot;:&quot;%E5%86%B7%E5%B3%B0%E6%AE%8B%E9%9B%AA&amp;ie=utf-8&quot;,&quot;user_sex&quot;:2,&quot;portrait&quot;:&quot;7c5ae586b7e5b3b0e6ae8be99baacb08&quot;,&quot;is_like&quot;:1,&quot;level_id&quot;:8,&quot;level_name&quot;:&quot;\u6252\u76ae&quot;,&quot;cur_score&quot;:997,&quot;bawu&quot;:0,&quot;props&quot;:null},&quot;content&quot;:{&quot;post_id&quot;:72232792979,&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tieba&quot;,&quot;open_type&quot;:&quot;&quot;,&quot;date&quot;:&quot;2015-07-25 21:59&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:2,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:93,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:1,&quot;pb_tpoint&quot;:null}}"
print json.loads(s.replace('&quot','"')

json.dumps({'s':3,'t':4})



