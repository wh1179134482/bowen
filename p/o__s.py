#！usr/bin/python
#-*-coding:utf8-*-
import os
# a = os.getcwd()
# print(a)
#返回指定路径下所有文件和目录名，括号里填写  . () a 都是显示当前路径下的  '..'上一级
# list=os.listdir('.')
# print(list)
#删除指定路径下的文件
#delete = os.remove('a,jpg')
#创建递归目录
# dirs = os.mkdirs(r'111\222\333\444')
#只能删除指定录下的空目录,递归目录（前提目录是空的）
#delete_dir = os.removedirs(r'111\222\333\444')
#创建单级目录
# dir = os.mkdir('qqq')
#删除单级目录
# delete_dir=os.rmdir('qqq')
#判断指定路径下的名称是不是文件
# a = os.path.isfile('a.txt')
# print(a)
# #判断文件或者目录是否存在
# d = os.path.exists('')
# print(d)
# #判断路径下的名称是不是目录
# b = os.path.isdir('b.txt')
# print(b)
# #将路径分隔成路径名和文件名
c = os.path.split(r'D:\p\py_1906')
print(c)
# #连接目录与文件名或者目录
e = os.path.join('D:\\p', 'py_1906')
print(e)