#        循环
# -*- coding: UTF-8 -*-
# for i in range(1,5):
#   for j in range(1,5):
#     for k in range(1,5):
#       if(i!=j) and (i!=k) and (j!=k):
#           print(i,j,k)

#        ASKLL码
# name = input()
# result=chr(name)
# print(result)

# 不换行
# a ="1" 
# print(a,end="")
# print(a,end="")

#List
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])

#if
# age = input()
# s=int(age)
# if s>10:
#     print("ok")
# else:
#     print("no")

# L = list(range(5))
# sum = 0
# for i in L:
#     sum = sum+i
#     print(sum)

# d={'mcgrady':10,'kobe':20}
# a=d.get('mcgrad',-1)
# print(a)

# s = 'abc'
# b=s.replace('a','A')
# print(b)
# print(s)

# a = hex(10)
# print(a)

# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# a = input()
# print(my_abs(int(a)))
# def add_af(L=[]):
#   L.append('end')
#   return L
# print(add_af([1,2]))

# def calx(*number):
#     sum = 0
#     for i in number:
#         sum=sum+i*i
#     return sum
# L = [1,2,3]
# print(calx(L[0],L[1],L[2]))

# def person(name,age,**kx):
#    print('name:',name,'age:',age,'other:',kx)
# person('a',1,city='beij',na='ss')

# def person(a,b,c=0,*ars,**arsg):
#     print('a:',a,'b:',b,'c:',c,'ars:',ars,'arsg:',arsg)
# L=(1,2,3,4)
# person(1,2,3,'a','b','v',L,o='beij')
# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')
# def trim(s):
#    if s[:1]!=' ' and s[-1:]!=' ':
#        return s
#    elif s[:1]==' ':
#        return trim(s[1:])
#    else:
#        return trim(s[:-1])
# print(trim('    dsf    '))

# def trim(s):
#     for i in range(len(s)):
#         if s[0]==' ':
#             return s[1:]
#     for n in range(len(s)):
#         if s[-1]==' ':
#             return s[:-1]
# print(trim(' dd '))
# d = {'a': 1, 'b': 2, 'c': 3}
# for i in d.items():
#     print(i)
# def findMinAndMax(L):
#     max=L[0]
#     min=L[0]
#     for value in L:
#         if max<value:
#             max = value
#         if min>value:
#             min = value 
            
#     return (max,min)
# L=(1,2,3,4,7,10,5)
# print(findMinAndMax(L))
# L=[x*x for x in range(1,10) if x%2==0]

# print(L)

# L = [i+j+z for i in 'ABC' for j in 'abc' for z in '123']
# print(L)
# import os
# L=[d for d in os.listdir('.')]
# print(L)

# d={'x':'A','y':'B'}
# for key in d.items():
#     print("key=",key)

# L = ['DFDSF','DFDSF','FDFGDF']
# print([i.lower() for i in L])

# x = int(input("请输入第一个数"))
# y = int(input("请输入第二个数"))
# z = int(input("请输入第三个数"))
# a=(x if x>y else y) if (x if x>y else y)>z else z
# print(a)

# L = (i for i in range(10))
# for z in L:
#     print(z)

# def fib(max):
#     a,b,c,i=1,1,0,0
#     while i<max:
#         i=i+1         
#         if i==0:
#             print(1)
#         elif i==1:
#             print(1)
#         else:
#             c = a+b
#             b = a
#             a = c
#             print(c)
 
# fib(int(10))
# class Student(object):
#     print('hhh')
#     pass
# bart = Student()
# bart.name = 'mc'
# print(bart.name)
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score = score
# bart = Student('mc',60)
# print(bart.name)
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())
# class Student(object):
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#     def set_gender(self,gender):
#         self.gender = gender
#     def get_gender(self):
#         return self.gender
# bart = Student('Bart', 'male')
# print(bart.get_gender())
# if bart.get_gender() != 'male':
#     print('1测试失败!')
# else:
#     bart.set_gender('female')
#     print(bart.get_gender())
#     if bart.get_gender() != 'female':
#         print('2测试失败!')
#     else:
#         print('测试成功!')
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# def run_twice(animal):
#     animal.run()
#     animal.run()

# a = Animal()
# d = Dog()
# c = Cat()

# print('a is Animal?', isinstance(a, Animal))
# print('a is Dog?', isinstance(a, Dog))
# print('a is Cat?', isinstance(a, Cat))

# print('d is Animal?', isinstance(d, Animal))
# print('d is Dog?', isinstance(d, Dog))
# print('d is Cat?', isinstance(d, Cat))
# print('c is Cat?', isinstance(c, Cat))
# run_twice(a)
# class Student(object):
    
#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#         return self._score
# L = Student()
# print(L.set_score(4))   
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def _str_(self):
#         return 'student:%s' % self.name
# print(Student('mc')._str_())




# 问题1 class的执行顺序
# class stdent(object):
#     def __init__(self):
#         print('init')
#     def main(self):
#         print('main')
#     def fun(self):
#         print('fun')
    
# L =stdent()
# L.main()
#问题2 for n in Fib() 执行顺序
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         print('aa')
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
# for n in Fib():
#     print(n)

#问题3
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# f = Fib()
# print(f[0])

# class Student(object):
#     def __getattribute__(self,att):
#         if att=='name':
#             return lambda:5
#         else:
#             return 1
#     def st(self):
#         return 1
# print(Student().st)
# from enum import Enum,unique
# @unique
# class Week(Enum):
#     sun=0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# print(Week.Mon.value)
# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('END')
# with open('D:\hello.txt','r') as f:
#     for line in f.readlines():
#         print(line.strip())
# with open('D:\hello.txt', 'a') as f:
#     f.write('Hello, world!!')

# from io import StringIO
# f=StringIO()
# f.write('hello')
# print(f.getvalue())
# from io import BytesIO
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# import os
# print(os.path.abspath('.'))
# import json
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score = score
# def studentlist(self):
#         return{
#             'name':self.name,
#             'score':self.score
#         }    
# L= Student('mcgrady',90)
# print(json.dumps(L,default=studentlist))
# import multiprocessing as mp
# import os

# def run_proc(name):
#     print('aaaaa %s(%s)' %(name,os.getpid()))

# if __name__ == "__main__":
#     print('Parent process %s.' % os.getpid())
#     p = mp.Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == "__main__":
#     print('1111:%s'%os.getpid())
#     p=Pool(5)
#     for i in range(10):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('end')




















# import urllib
# import urllib.request
# from bs4 import BeautifulSoup
# import re
# import random
# import time

# if __name__ == "__main__":
#     # 设置目标url，使用urllib.request.Request创建请求
#     url0 = "http://newcar.xcar.com.cn/257/review/0.htm"
#     req0 = urllib.request.Request(url0)

#     # 使用add_header设置请求头，将代码伪装成浏览器
#     req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")

#     # 使用urllib.request.urlopen打开页面，使用read方法保存html代码
#     html0 = urllib.request.urlopen(req0).read()

#     # 使用BeautifulSoup创建html代码的BeautifulSoup实例，存为soup0
#     soup0 = BeautifulSoup(html0)

#     # 获取尾页（对照前一小节获取尾页的内容看你就明白了）
#     total_page = int(soup0.find("div",class_= "pagers").findAll("a")[-2].get_text())
#     myfile = open("aika_qc_gn_1_1_1.txt","a")
#     print("user","来源","认为有用人数","类型","评论时间","comment",sep="|",file=myfile)
#     for i in list(range(1,total_page+1)):
#         # 设置随机暂停时间
#         stop = random.uniform(1, 3)
#         url = "http://newcar.xcar.com.cn/257/review/0/0_" + str(i) + ".htm"
#         req = urllib.request.Request(url)
#         req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
#         html = urllib.request.urlopen(req).read()
#         soup = BeautifulSoup(html)
#         contents = soup.find('div', class_="review_comments").findAll("dl")
#         l = len(contents)
#         for content in contents:
#             tiaoshu = contents.index(content)
#             try:
#                 ss = "正在爬取第%d页的第%d的评论，网址为%s" % (i, tiaoshu + 1, url)
#                 print(ss)
#                 try:
#                     comment_jiaodu = content.find("dt").find("em").find("a").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
#                 except:
#                     comment_jiaodu = ""
#                 try:
#                     comment_type0 = content.find("dt").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
#                     comment_type1 = comment_type0.split("【")[1]
#                     comment_type = comment_type1.split("】")[0]
#                 except:
#                     comment_type = "好评"
#                 # 认为该条评价有用的人数
#                 try:
#                     useful = int(content.find("dd").find("div",class_ = "useful").find("i").find("span").get_text().strip().replace("\n","").replace("\t","").replace("\r",""))
#                 except:
#                     useful = ""
#                 # 评论来源
#                 try:
#                     comment_region = content.find("dd").find("p").find("a").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
#                 except:
#                     comment_region = ""
#                 # 评论者名称
#                 try:
#                     user = content.find("dd").find("p").get_text().strip().replace("\n","").replace("\t","").replace("\r","").split("：")[-1]
#                 except:
#                     user = ""
#                 # 评论内容
#                 try:
#                     comment_url = content.find('dt').findAll('a')[-1]['href']
#                     urlc = comment_url
#                     reqc = urllib.request.Request(urlc)
#                     reqc.add_header("User-Agent",
#                                     "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
#                     htmlc = urllib.request.urlopen(reqc).read()
#                     soupc = BeautifulSoup(htmlc)
#                     comment0 = \
#                     soupc.find('div', id='mainNew').find('div', class_='maintable').findAll('form')[1].find('table',class_='t_msg').findAll('tr')[1]
#                     try:
#                         comment = comment0.find('font').get_text().strip().replace("\n", "").replace("\t", "")
#                     except:
#                         comment = ""
#                     try:
#                         comment_time = soupc.find('div', id='mainNew').find('div', class_='maintable').findAll('form')[1].find('table', class_='t_msg').\
#                         find('div', style='padding-top: 4px;float:left').get_text().strip().replace("\n","").replace( "\t", "")[4:]
#                     except:
#                         comment_time = ""
#                 except:
#                     try:
#                         comment = content.find("dd").get_text().split("\n")[-1].split('\r')[-1].strip().replace("\n", "").replace("\t","").replace("\r", "").split("：")[-1]
#                     except:
#                         comment = ""
#                 # time.sleep(stop)
#                 print(user,comment_region,useful,comment_type,comment_time,comment, sep="|", file=myfile)
#             except:
#                 s = "爬取第%d页的第%d的评论失败，网址为%s" % (i, tiaoshu + 1, url)
#                 print(s)
#                 pass

    


    # import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...%s' % (threading.current_thread().name,1))
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# import re
# if re.match(r'\d{9,11}@qq\.com','467771692@qq.com'):
#     print('T')

# class Query(object):
    
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)

# from urllib import request, parse
# import numpy
# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))
# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# import random
# #随机字母
# def rndChar():
#     return chr(random.randint(65,90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# # 240 x 60:
# width = 60*4
# height = 60
# image = Image.new('RGB',(width,height),(255, 255, 255))
# # 创建一个font对象
# font = ImageFont.truetype('/Library/Fonts/Arial.tt', 36)
# # 创建一个draw对象
# draw= ImageDraw.Draw(image)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())
# # 输出文字
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
# 导入turtle包的所有内容:
# from turtle import *

# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)

# for x in range(0, 250, 50):
#     drawStar(x, 0)
# done()
# 设置笔刷宽度:
# width(100)

# # 前进:
# forward(200)

# # 右转90度:
# right(90)

# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)

# pencolor('green')
# forward(200)
# right(90)

# pencolor('blue')
# forward(100)
# right(90)

# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()
# from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()

import socket
#创建一个
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)