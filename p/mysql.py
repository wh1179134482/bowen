#！usr/bin/python
#-*-coding:utf8-*-
import pymysql
#192.168.10.255
#链接mysql，host：mysql所在的主机地址，user：mysql用户，password：密码 pord：mysql数据库端口号
connect = pymysql.connect(host='192.168.10.168',user='root',password='123456',pord=3306)
#创建游标，一种临时的数据库对象，相当于购物车
cusor = connect.cursor()
#执行操作
#cusor.execute('create database weng')
cusor.execute('use weng;')
# cusor.execute('create table stu(name char(20),age int);')
# cusor.execute('insert into stu values("{}","{}");'.format())1
cusor.execute('select * from stu;')
#fetchone查看数据库表中一行数据，可迭代
data = cusor.fetchone()
print(data)
#去表中所有的数据
# data = cusor.fetchall()
# print(data)
#
# data_1 = cusor.fetchmany()#括号填数字显示几个
# print(data_1)
#提交数据，在插入数据的时候一定要提交，
# 否者提交的数据就不会被提交，只会被保存在临时数据库中
connect.commit()
#断开连接
connect.close()