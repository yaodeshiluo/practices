# -*- coding: utf-8 -*-
import requests
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

commentid = '0'
url = 'http://sns.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=p0195oqpagu'
response = requests.get(url)
cmt_id = re.search(r'"comment_id":"(\d*)"' ,response.text).group(1)
print cmt_id

url_cmt = 'http://coral.qq.com/article/%s/comment?commentid=%s&reqnum=10' % (cmt_id ,commentid)
print url_cmt
headers = \
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
response_cmt = requests.get(url_cmt, headers=headers)
print response_cmt.text
comments = json.loads(response_cmt.text)
print comments
comments_list = comments['data']['commentid']
f = open(u'黑甲.txt', 'a')  # test
for i in range(len(comments_list)):
    # i = 0 #test
    nick = comments_list[i]['userinfo']['nick']
    time = comments_list[i]['timeDifference']
    region = comments_list[i]['userinfo']['region']
    content = comments_list[i]['content']
    f.write(nick + '  ')
    f.write(time + '  ')
    f.write(region + '\n')
    f.write(content + '\n\n')
f.close()  # test
commentid = comments_list[9]['id']