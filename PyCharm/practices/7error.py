#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError: #亲测这里的e可以删掉。 错误处理代码，即except语句块
    print 'except:', e #print后面的 ，号表示的是空格，后面接变量是指显示这个变量的值。
finally:
    print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e: #亲测这里的e删了后，下面代码运行正常，但pycharm会提示说unresolved reference
    print 'ValueError:', e
except ZeroDivisionError, e: #except语句块可以有多个，按顺序执行，
    print 'ZeroDivisionError:', e
else: #可有可无
    print 'no error!'
finally: #必然会执行的语句块，可有可无
    print 'finally...'
print 'END'
#亲测Python所有的错误都是从BaseException类派生

try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e: #第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类
    print 'ValueError'

def main(): #检查错误的函数，函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
#错误是class，捕获一个错误就是捕获到该class的一个实例——看颜色
#我们自己编写的函数也可以抛出错误：
class FooError(StandardError): #错误的子类，BaseException也行
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' %s)
    return  10/n
foo('0')

def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise #raise语句如果不带参数，就会把当前错误原样抛出 #

def main():
    bar('0')

main()
#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #! = 表示不等于，还可以写成not (n == 0)。assert直接接'n is zero!'的话，这一行代码不运行？？
    return 10 / n

def main():
    foo('0')
