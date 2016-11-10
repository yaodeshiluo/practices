# -*- coding: utf-8 -*-
# import sys
# print sys.getdefaultencoding()
# sys.getfilesystemencoding()
#
#
#
# s= u'8'
# s1 = s.encode('gbk')
# print isinstance(s1,str)
#
# print int.__doc__
#
# import sys
# i = 'hello world'
# for each in i:
#     print each,
#
# for i in enumerate('jfdosofja '):
#     print i, type(i)
#
# for item in ['1','2','3']:
#     print item,
#     print
#
# list = [2,37.8,92,1,77,66,2]
# def sort_insert(list):
#     '''插入法排序'''
#     for i in range(1,len(list)):
#         while i > 0:
#             if list[i] < list[i-1] :
#                 a = list[i-1]
#                 b = list[i]
#                 list[i-1] = b
#                 list[i] = a
#             i -= 1
#     return list
#
# sort_insert(list)
# print list
#
#
# list = [2,37.8,92,01,77,88,2,74,6]
# def sort_bubble(list):
#     '''冒泡法排序'''
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[j] < list[i]:
#                 a = list[i]
#                 b = list[j]
#                 list[i] = b
#                 list[j] = a
#     return list
# sort_bubble(list)
# print list

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

url_cmt = 'http://coral.qq.com/article/1377491570/comment?commentid=6198494899164599792&reqnum=20' #% (cmt_id ,commentid)
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
