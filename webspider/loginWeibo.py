import requests
from lxml import etree

url = 'http://www.500d.me/login.jhtml'
# html = requests.get(url).content
# print html
# sel = etree.HTML(html)
s = '''Cookie: Hm_lvt_3e432021fa3cef1b8b58965a002fd8c9=1469373755; Hm_lpvt_3e432021fa3cef1b8b58965a002fd8c9=1469375893; Hm_lvt_f2a5f48af9d935f4001ca4c8850ce7c0=1469373755; Hm_lpvt_f2a5f48af9d935f4001ca4c8850ce7c0=1469375893; _ga=GA1.2.543984886.1469373787; _gat=1
'''

cook = 'JSESSIONID=4575AC8B451FEB18C66739C1F895CAC4; token=774f0e23-16c9-421f-8cde-f88e9ecf08d0; memberIsVIP=false; cartSize=0; rememberEmail=344098585%40qq.com; qs_lvt_8148=1469373754; memberHead=http%3A%2F%2Fstatic.500d.me%2Fresources%2F500d%2Fimages%2Fdefault.jpg; memberName=%E6%88%91%E7%9A%84%E4%BA%94%E7%99%BE%E4%B8%81; memberEmail=344098585%40qq.com; memberSafeKey=2828af1b5be5746b4b8c63493006fc7d; Hm_lvt_3e432021fa3cef1b8b58965a002fd8c9=1469373755; Hm_lpvt_3e432021fa3cef1b8b58965a002fd8c9=1469376255; Hm_lvt_f2a5f48af9d935f4001ca4c8850ce7c0=1469373755; Hm_lpvt_f2a5f48af9d935f4001ca4c8850ce7c0=1469376255; _ga=GA1.2.543984886.1469373787'
data = {'Cookie':cook}
# s2 = s.split('\n')
# if '' in s2:
#     s2.remove('')
# data = {}
# for i in s2:
#     s3 = i.split(':',1)
#     data[s3[0].strip()] = s3[1].strip()
# print data

html = requests.get(url,cookies = data).content
print html