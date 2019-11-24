#！usr/bin/python
#-*-coding:utf8-*-
#1支持索引
# a = 'abc'
# print(a[0])


# a = 'abcdefg'
#一个冒号
#1:下标号后加冒号，表示显示从下标号开始到结尾。
# print(a[::-2])
#如果“-2”负几就是显示后几位，就是显示后两位。
# print(a[-2:])
#下标号前加冒号，表示显示从下标号前一位开始到开头。
# print(a[:2])
#下标号前加冒号，表示不显示最后一位。
# print(a[:-1])
#两者结合，显示从开始值到结尾值（结尾值不显示），后者要比前者大
# print(a[1:3])


#  两个冒号时
# 1:将下标放在冒号前，显示从下标对应的字符开始到结尾
# print(a[2::])
# 2:将下标号放在冒号后，以下标号分组默认取组中第一个
# print(a[::2])
# 3:两者结合，以三位数为一组，显示组中第三个
# print(a[1::2])

# while 1:
#     i = input("请输入一个数：")
#     if i >= "90" and i < "100":
#         print("优秀")
#     elif i >= "70" and i < "90":
#         print("良好")
#     elif i >= "60" and i <"70":
#         print("及格")
#     else:
#         print("不及格")


# i = input("请输入一个数：")
# if "a" in i and "b" in i:
#     print("123")
# elif "a" in i :
#     print("456")
# elif "b" in i :
#     print("789")
# else:
#     print("没了")

# i = input("判断烤地瓜熟了没，(0-2级是生的，5级是熟的，8级以上就焦了):")
# if "0" >= i <= "2" :
#     print("生的")
# elif "4" >= i >="2":
#     print("半生不熟")
# elif "8" >= i <= "5":
#     print("熟的")
# else:
#     print("焦了")
#1.'''upper()将小写变大写'''
# b = input("请输入一个小写字符：")
# a = b.upper()
# print(a)
# 2.'''lower()将大写变小写'''
# b = input("输入一串字符：")
# a = b.lower()
# print(a)
'''3.title()将首字母大写'''
# b = input("输入一串字符：")
# a = b.title()
# print(a)
'''4.swapcase():大小写相互转换'''
# b = input("输入一串字符：")
# a = b.swapcase()
# print(a)
'''5.将字符串中的字符替换为其他数据：replace('原内容','替换内容',替换数量)'''
# a = '151617'
# b = a.replace('1','q',2)
# print(b)
'''6.以括号中的数据为分隔符，将字符串分隔成列表:split('分割符')'''
# a = '151617'
# b = a.split('1')
# print(b)
'''7.以某个数据将列表连接起来形成新的字符串 分隔符。 join(元素序列)'''
# a = 'wewdeffedrgegdberbwdfrbr'
# b = a.split('d')
# c = '-'.join(b)
# print(c)
'''8.startswith(字符串)：判断是否以括号中的字符串的开头'''
# a = 'addd'.startswith('b')
# print(a)

'''1."%" %填的字符  %s：通过str()将输入的字符转化成字符串 %d整数 %f浮点数'''
# b = 0
# for a in range(1,101):
#      if a % 2 == 0:
#          b= b + a
# print(b)
# b = 0
# for a in range(1,101,2):
     # if a % 2 == 1:
#          b= b + a
# print(b)
# a = ['abc','ABc','abb','cda']
# for b in a:
#    if (b.startswith('a') or b.startswith('A')) and b.endswith('c'):
#     print(b)

# b = [11,22,33,44,55,66,77,88,99]
# c = []
# d = []
# for i in b:
#  if i > 55:
#   c.append(i)
#  elif i < 55:
#   d.append(i)
# print(c)
# print(d)

# while 1:
#  i = input("请输入一个字符串：")
#  if i == 'exit':
#    break
#  i = i.replace(' ', '').title().replace('a','123')
#  print(i)

# a = [1,23,3,4,4,5,6,7,8,8,4,4]
# j = []
# for i in a :
#     if i not in j :
#         j.append(i)
# print(j)
# for i in a:
#     if a.count(i) > 1:
#         for j in range(a.count(i)-1):
#             a.remove(i)
# print(a)


# for i in range(1,101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i,end="\t")

'''三次比大小'''
import random
# a = random.randint(1, 10)
# for j in range(3):
#     i = int(input("请猜牌："))
#     if i > a :
#         if i == 0:
#             continue
#         print("大">,你还有%d机会" % (2-j))
#     elif i < a :
#         if i == 0:
#             continue
#         print("小了，你还有%d次机会" % (2-j))
#     else:
#         print("奖励五块钱")
#         break
# else:
#         print("你是废物")

# for a in range(1,51):
#     print("user%d"%a,end="\t")

# a = input("请输入一组数据(注意用隔开)：")
# b = a.split(" ")
# c = []
# for j in b:
#     c.append(int(j))
# for i in range(len(c)-1):
#     for k in range(len(c)-1):
#         if c[k] > c[k+1]:
#             c[k],c[k+1] = c[k+1],c[k]
# print(c)
# try:
#     print('执行了try语句')
#     a = '123'
#     int(a)
# except Exception as b:
#     print('执行了except语句')
# else:
#     print('执行了 else语句')
# finally:
#     print('执行了finally语句')

# try:
#     a = 'sca'
#     int(a)
#     raise TypeError('这是类型错误')
# except Exception as e :
#     print(e)