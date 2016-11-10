# coding=utf-8
# 使用__slots__:
class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name


# 给实例绑定一个方法：利用MethodType动态给class加上功能
def set_age(self, age):
    self.age = age  # 测试这里把self换成p，下面的运行仍然成立。


def set_age(self):
    self.age = 18  # 将这个方法绑定给实例后，s.set_age(25)会报错为TypeError: set_age() takes exactly 1 argument (2 given)！


def print_age(self):  # 这个方法也能绑定给实例
    print 'age: 25'


set_age('Michael', 89)  # AttributeError: 'str' object has no attribute 'age'

from types import MethodType

s.set_age = MethodType(set_age, s, Student)
s.print_age = MethodType(print_age, s, Student)
s.set_age(25)
s.age

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
s2.set_age(25)  # AttributeError: 'Student' object has no attribute 'set_age'


# 给所有实例绑定方法。
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, None, Student)
Student.city = 'Beijing'  # 亲测，可以给所有实例加上属性！


# 动态加上属性和方法见上所示。用__slots__可以进行一定限制。
class Student(object):
    __slots__ = ('name', 'age')  # 注意格式，tuple里加属性名称


s = Student()
s.name = 'Job'
s.age = 23
s.score = 99  # 报错


# __slot__对继承的子类不起作用！！！！
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99  # 不会报错。


# 在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
    __slots__ = ('name')  # 含有'name' 'age'两个属性。


# 限制score的范围
class Student(object):
    def __init__(self, name, age, score):  # 四个参数，a = Student('Michael', 25, 99)。如果直接用__slot__的话，就可以直接s = Student()
        self.name = name
        self.age = age
        self.score = score

    def get_score(self):  # 从颜色来看，__init__不像是一般函数，下面的函数名都是红色。
        return self.score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self.score = value  # 改用else其实效果一样。


s = Student()  # 报错，TypeError: __init__() takes exactly 4 arguments (1 given)
a = Student('Michael', 25, 99)


# @property可以将一个getter方法变成属性，方法  到  属性。参考上面。一个getter方法，一个setter方法。
class Student(object):
    def __init__(self, name, age, score):  # 四个参数，a = Student('Michael', 25, 99)。如果直接用__slot__的话，就可以直接s = Student()
        self.name = name
        self.age = age
        self.score = score

    @property
    def fenshu(self):  # 成功将一个函数变成属性！！！！！但fenshu.setter没成功，会报错。
        return self.score

    @property  # 如果只有这一行，没有@score.setter，score将成只读性性，上面的self.score会报错， a = Student('Michael', 25, 99)也会报错说无法set ttribute.
    def score(self):
        return self.score

    @score.setter  # 有了这一行，score就不是只读属性，是可读写属性。
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value  # 这一行必须是self._score,而不能是self.score，不然递归错误！！！！！！？？？？？？RuntimeError: maximum recursion depth exceeded


a = Student('Michael', 23, 99)


class Gs(object):
    @property
    def score(self):
        return self._score  # score前没有下划线,d.score会报递归错误！！！！？？？？另外，有下划线，则说无 'Gs' object has no attribute '_score'

    @score.setter  # 即使这个类里面没有定义score属性，但输入d.score = 999会报错，输入d.score = 99后，d.score 结果为99
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value  # 如果这里的score前没有下划线，上面的_score会说pycharm Unresolved attribute reference '_score' for class 'Gs'可见这两部分相互依存。另外输入d.score = 99 后会报递归错误！！！！？？？


d = Gs()

# 定制类，用一些特殊的函数，如__len__()方法我们也知道是为了能让class作用于len()函数。特殊函数是否可以理解为即使不定制也会有默认输出结果的函数呢？
class Student(object):
    def __init__(self,name):
        self.name = name

print Student('Michael')
s = Student('Job')
print s
s.__str__() #即使没有定义，仍然有效。通过重新定义，可以改变输出结果。
s.__repr__()


#使用__str__可以使得print s显示字符串，这么理解？？特殊函数呈蓝色状！！！！
class Student(object):
    def __init__(self,name): #定制初始属性
        self.name = name
    def __str__(self): #定制print的输出结果
        return 'Student object (name: %s)' %self.name #注意是return
    def __repr__(self): #定制开发者看到的结果
        return 'name:  %s)' %self.name # 可以直接写 __repr__=__str__ ，也可以再定义一个__repr__()

#但输入s或是Student('Michael')后调用的是__repr__(),结果是开发者看到的字符串。print s调用的是__str__,用户看到的字符串。

#__iter__,可以将类定制成类似list或是tuple的可迭代的类，从而可以被用于for  in 循环、
class Fib(object): #可以理解为三步走吗？
    def __init__(self):
        self.a, self.b = 0, 1 #初始化的两个值
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def next(self): #特殊函数都是蓝色的，next在这里也是特殊函数？？？？？
        self.a, self.b = self.b, self.a + self.b # 计算下一个值,每运行一次s.next(),self.a, self.b 的值会发生相应变化，从而保存下来。#不能用a, b = 0, 1, a, b = b, a+b来替代，因为只能说明逻辑，不能保存数值。
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

s = Fib()
s.a # 1
s.b
s.next()
s.next()
s.a
s.b

for i in Fib():
    print i

Fib()[5] #报错，说明Fib()虽然可以迭代，但不是list也不是tuple

class Fib(object): #是否一个类下面只有一个实例？？类抽象描述，但满足这种抽象描述的可能只有一个实例？？或者说类只是对某个实例的抽象描述，类本身只是一种描述，只有具体的实例才有意义。
    def __getitem__(self, n): #定制Fib()[n]的输出结果
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib() #f是满足Fib()所抽象描述的类的一个实例。类只是一种抽象描述，这里的=号是指实例满足这种抽象描述！！！
f[0]
f[2]
#定制Fib的切片，但没有对step参数作处理，也没有对负数作处理。
#通过__setitem__(),__delitem__等方法，可将我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a, b = 1, 1
            for x in range(n): #range(0)为[], for循环未运行。
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop #slice类自带属性？
            a, b = 1, 1
            L= []
            for x in range(stop):
                if x>= start:
                    L.append(a) #这里的if代码块和下面的a, b = b, a+b换位置后，结果大不同！！！
                a, b = b, a+b
            return L

Fib()[2:8]
Fib().__getitem__(8)

for i in Fib():
    print i #用上述方法可以切片，也能迭代。但没上限，可改成下面

for i in Fib()[:8]:
    print i


#写一个__getattr__()方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self,attr): #注意，前面和后面都是双下划线，不然不呈蓝色。
        if attr == 'score': #注意是==
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)



s = Student()
s.age
s.age()
s.score
s.abc #返回None，而不是报错。

#元类
import sys #直接就导入了，没有从哪里？？？
sys.path.append('D:\PyCharm\practices') #没有这一步的话，下面会出错。
from hello import Hello #从hello.py里导入Hello类, 从某个模块里导入
h = Hello()
h.hello()
print(type(Hello)) #Hello是一个class，它的类型就是type  向上一级？？
print(type(h)) #h是一个实例，它的类型就是class Hello。  向上一级？？

#type() 不仅可以返回类型，而可以创建出新的类型， 除class之外！
def fn(self,name= 'world'): #先定义函数 这里亲测把self换成a都行？？！！
    print('Helo, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn)) #要创建一个class对象，type()函数依次传入3个参数：class的名称； 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法； class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#元类：先定义metaclass，就可以创建类，最后创建实例。类看成是metaclass创建出来的“实例”。

def pri(self):
    print self
class Tu(object):
    pass
s=Tu()
s.pri = pri
