from Tkinter import *
import tkMessageBox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello,%s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()




import mysql.connector
conn=mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor=conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
cursor.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
cursor.close()
conn.close()

def application(environ, start_response):
    start_response('200 0K', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'

import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

c = consumer()


class Student(object):
    def __int__(self,name, score):
        self.__name = name
        self.__score = score
    def print_score(self): #方法的第一个参数是self，直接参数则与普通函数类似。
        print '%s: %s' % (self.__name, self.__score) #注意，是__self.name!!
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

