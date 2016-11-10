# coding=utf-8
f=open('D:\\PyCharm\\practices\\test.txt')
f.read()
f=open(r'D:\PyCharm\practices\test.txt','r') #有转义符，\t有意义，前面加r,或者两个\\
#mac操作系统下目录为'/Users/michael'，是/，不是\
#每次打开提取数值之后就关闭，这样少占用系统资源。
try
    f=open(r'D:\PyCharm\practices\test.txt','r')
    print f.read()
finally:
    if f:
        f.close()
#相当于以下代码：
with open(r"D:\PyCharm\practices\test.txt",'r') as f: #亲测标识符删了也行啊
    print f.readline()
    print f.readline()
    print f.readline() #结果三行之间有空行，因为第一行最后代码都是/n

with open(r"D:\PyCharm\practices\test.txt",'r') as f:
    for line in f.readlines():
        print line.strip() # 把末尾的'\n'删掉


f.read()
#标识符'r'或者'rb'表示输出文本文件或输出二进制文件？？
#标识符'w'或者'wb'表示写文本文件或写二进制文件
f=open(r'D:\PyCharm\practices\test.txt','w')
f.write('hello,world') #只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
f.read() #IOError: File not open for reading
f.close()
f=open(r'D:\PyCharm\practices\test.txt','r')
f.read()
f.read()#两次打开结果不一样？？！！！！

#文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯：
with open(r'D:\PyCharm\practices\test.txt','w') as f:
    f.write('hello,world\ngodlike\nhollyshit\ndouble kill\nsilly')

with open(r"D:\PyCharm\practices\test.txt",'r') as f:
    print f.read()

#操作文件和目录
import os
os.name #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
os.environ['PATH']
os.getenv('PATH')

# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')

os.rename('D:\PyCharm\practices\holly.txt','holly.py') #文件跑PyCarm下了
os.remove('test.py')

#把  变量  从内存中  变成可存储或传输的过程称之为序列化，在Python中叫pickling
#pickling序列化.Python提供两个模块来实现序列化：
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

#pickle.dump()直接把对象序列化后写入一个file-like Object
d = dict(name='Bob', age=20, score=88)
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
#用pickle.loads()方法反序列化出对象
pickle.loads("(dp1\nS'age'\np2\nI20\nsS'score'\np3\nI88\nsS'name'\np4\nS'Bob'\np5\ns.")
#直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
f=open('dump.txt', 'rb')
d=pickle.load(f)
f.close()
#这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

#json
#dumps()方法返回一个str
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
#同理
#类似的，dump()方法可以直接把JSON写入一个file-like Object。
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str) #{u'age': 20, u'score': 88, u'name': u'Bob'}

import json
d = dict(name='Bob', age=20, score=88)
f=open('dump.txt','wb')
json.dump(d,f)
f.close()
#反序列
f=open('dump.txt', 'rb')
d=json.load(f)
f.close()
d #{u'age': 20, u'score': 88, u'name': u'Bob'}

#默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

#这两种写法等价
def student2dict(std):
    return {'name': std.name,'age': std.age,'score': std.score}

print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
print(json.dumps(s.__dict__))

#把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))





