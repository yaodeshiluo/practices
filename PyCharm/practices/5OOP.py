#!/usr/bin/env python
# -*- coding: utf-8 -*-


#在Python中，所有数据类型都可以视为对象，当然也可以自定义对象class
#面向对象的设计思想是抽象出Class，根据类Class创建实例Instance。先Class，后Instance。

class Student(object):
    def __init__(self, name, score): #上面空了一行，结果报错
        self.name = name
        self.score = score
    def print_score(self):  #上面空了一行，结果报错
        print '%s: %s' % (self.name, self.score)


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score
lisa.print_score()


#类抽象，实例具体
#创建实例是通过类名+()实现的
class Student(object):
    pass

bart = Student() #变量bart指向的就是一个Student的object
bart

bart.name = 'Bart Simpson'
bart.name



class Student(object):
    def __init__(self, name, score): #这一行上不能有空行，报错！！
        self.name = name  #绑定属性
        self.score = score


bart = Student('Bart Simpson', 59)
bart.name
bart.score

#类的方法。定义一个方法：第一个参数是self。除了self不用传递，其他参数正常传入：
#方法就是与实例绑定的函数(bound method Student.get_grade)，和普通函数不同，方法可以直接访问实例的数据

class Student(object):
    def __init__(self, name, score): #这一行上不能有空行，报错！！
        self.name = name  #绑定属性
        self.score = score
    def print_score(self):
        print '%s: %s' %(self.name, self.score) #不能是name,score 而是self.name,self.score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
bart.name
bart.score
bart.print_score
bart.print_score()
bart.get_grade
bart.get_grade()
bart = Student('Bart Simpson', 98) # 操作了数据


#和静态语言不同，Python允许对实例变量绑定任何数据
#同一个类的不同实例，但拥有的变量名称都可能不同：
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
bart.age # 8
lisa.age # 报错。AttributeError: 'Student' object has no attribute 'age'


#在Class内部，可以有属性和方法
#外部代码可以通过调用方法 操作数据。

#两个下划线__， 私有变量（private）——其实是不同版本的Python解释器可能会把__name改成不同的变量名，如改成_Student__name
class Student(object):
    def __int__(self,name, score):
        self.__name = name
        self.__score = score
    def print_score(self): #方法的第一个参数是self，直接参数则与普通函数类似。
        print '%s: %s' % (__self.name, __self.score) #注意，是__self.name!!
    def get_name(self): #允许外部代码获取name和score
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def set_name(self,name):
        self.__name = name

bart = Student('Bart Simpson', 98) # takes no parameters
bart.__name #已经无法从外部访问实例变量.__name和实例变量.__score了：
bart.name #'已经无法从外部访问实例变量.__name和实例变量.__score了：

#这样添加object：
bart = Student()
bart
bart.set_name('Bart Simpson')
bart.set_score(98) #注意不是set_score(bart, 98),  def set_score(self, score)里的第一个参数self自动代入。
bart.set_name('Bart Simpson')
bart.name #AttributeError
bart.__name #AttributeError
bart.get_name()
bart.get_score()
bart.set_score(1000) #raise ValueError


#以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的,    别用__name__等
#一个下划线开头的实例变量名，比如_name——虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

#继承和多态
#子类 subclass    父类、超类（Base class, Super class）

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run() #子类获得了父类的全部功能。
cat = Cat()
cat.run() #子类获得了父类的全部功能。

#对子类进行改进
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal): #两个class之间要有空行，不然报错
    def run(self):
        print 'Cat is running...'

dog = Dog()
cat = Cat() #这两行不加的话，以下两行的执行结果还是 Animal is running...  动态语言？？？
cat.run()  #子类的run()覆盖了父类的run()
dog.run()  #子类的run()覆盖了父类的run()

#定义一个class的时候，我们实际上就定义了一种数据类型
a = list() # a是list类型
a #[]
b = Animal() # b是Animal类型
Animal() #表示一个属于类Animal下的实例
b # <__main__.Animal object at 0x022023F0>
c = Dog() # c是Dog类型
c #<__main__.Animal object at 0x022023F0>


isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)
isinstance(c, Animal) #继承

def run_twice(animal): #def函数内部可修改变量（score），可定义属性（.name），可运行其他函数（如下），可print，可return。
    animal.run()
    animal.run() #具体调用的run()方法运行两次

run_twice(Animal())
run_twice(Dog()) #run()方法的种类多态！

#获取对象信息type() isinstance()
type(123)
type('str')
type(None)
type(abs)
type(Animal())

type(123)==type(456) #True
type('123')==type('abc') #True

import types
type('abc')==types.StringType
type(u'abc')==types.UnicodeType
type([])==types.ListType
type(str)==type(int)==types.TypeType #所有类类型本身的类型就是TypeType

#能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a',str)
isinstance(u'a',unicode)
isinstance(123,int)
#还可以判断一个变量是否是某些类型中的一种
isinstance('a',(str,unicode)) #等同于isinstance('a',basestring)

#要获得一个对象的所有属性和方法 dir()
dir('abc')
dir('ABC')
dir(str) #这三者得到的结果的一样

#__xxx__有特殊用途的属性和方法
len('ABC')
'ABC'.__len__()
'ABC'.len() #报错AttributeError

#看以下两个的不同。
class MyObject(object):
    def len(self):
        return 10

f=MyObject()
len(f) #报错！！！只能f.len()
#但是
class MyObject(object):
    def __len__(self): #跟上面比多了下划线
        return 10

f=MyObject()
len(f)  #特殊之处？？？
f.__len__()
f.len() #报错

#hasattr()    getattr()  setattr()
class MyObject(object):
    def __init__(self):
        self.x = 9 # 直接就赋值了，所以上面的参数只有一个
    def power(self):
        return self.x*self.x

obj=MyObject()
hasattr(obj,'x') #注意''
hasattr(obj,'y')
getattr(obj,'y')
getattr(obj,'y',404)
getattr(obj,'y','no') # 'no'

setattr(obj,'y',20)
hasattr(obj,'y')
getattr(obj,'y')
getattr(obj,'y',404)
getattr(obj,'y','no')

#获得对象的方法
hasattr(obj,'power')
getattr(obj,'power')
fn=getattr(obj,'power')
fn()



