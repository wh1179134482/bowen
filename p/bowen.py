# qq_number="1179134482"
# qq_password="123456"
# print(qq_password)

# a = 8.5  # 单价
# b = 7.5  # 重量
# c = a*b-5  # 价格
# print(c)

# name = "小明"
# age = 18
# sex = True
# hight = 1.75
# weight = 75.0
# print(type(age))
# a = 10
# b = True
# c = 8.8
# d = "zahngsan"
# f = "aaa"
# print(d + f)
# #
# a = float(input("请输入单价:"))
# b = float(input("请输入重量:"))
# c = a * b
# print("苹果的单价: %.2f元/斤,购买了: %.2f斤,需要支付: %.2f元" %(a,b,c))
#
# e = 25
# print("输出 %d" % e)
#
# name = "小明"
# student_no = 1
# a = float(input("请输入单价:"))
# b = float(input("请输入重量:"))
# c = a * b
# print("我的名字叫： %s 请多多关照,我的学号是： %06d,我去买苹果，苹果的单价: %.2f元/斤,购买了: %.2f斤,需要支付: %.2f元没钱了" %(name,student_no,a,b,c))
#
# student_no = 1
# print("我的学号是： %06d" % student_no)
#
# scale = 20
# print("数据比例是: %.3f%%" % scale)

# age = int(input("请输入你的年龄："))
# if age>0 and age<120:
#     print("Yes")
# else:
#     print("NO")

# python_score = int(input("输入你的python成绩:"))
# c_score = int(input("输入你的c成绩:"))
# if python_score > 60 or c_score > 60:
#     print("及格")
# else:
#     print("不及格")

# is_employee = True
# if not is_employee:
#     print("允许入内")
# else:
#     print("不允许入内")

# holiday_name=str(input("请输入节日："))
# if holiday_name == "情人节":
#     print("买玫瑰花")
# elif holiday_name == "平安夜":
#     print("买苹果")
# elif holiday_name == "生日":
#     print("买蛋糕")
# else:
#     print("每天都是jieri")提创可贴、

# has_ticket = int(input("是否有车票，1代表有，0代表没有："))
# if has_ticket:
#     print("可以进行安检")
#     knife_length = int(input("请输入刀的长度："))
#     if knife_length >= 20:
#         print("刀的长度为： %d cm 不允许上车" % knife_length)
#     else:
#         print("安检通过")
# else:
#     print("请购买车票")

# while True:
#     cj = float(input("请输入成绩："))
#     if cj >= 90 and cj <= 100:
#         print("优秀")
#     elif cj >= 70 and cj < 90:
#         print("一般")
#     elif cj >= 60 and cj < 70:
#         print("及格")
#     elif cj >= 0 and cj < 60:
#         print("不及格")
#     else:
#         print("请重新输入成绩")


# a = int(input("请输入一个数："))
# if a%2 == 0 and a%3 == 0:
#     print("helloworld")
# elif a%2 == 0:
#     print("hello")
# elif a%3 == 0:
#     print("world")
# else:
#     print("123")
# while 1:
#     a = int(input("请输入一个数："))
#     if a%2 == 0 or a%3 == 0:
#         if not a%2 == 0:
#             print("word")
#         elif not a%3 == 0:
#             print("hello")
#         else:
#             print("helloworld")
#     else:
#         print("123")

# import random
# while 1:
#     a = int(input("请出拳：(1代表拳头,2代表剪刀,3代表布)："))
#     b = random.randint(1,3)
#     print("电脑出拳：(1代表拳头,2代表剪刀,3代表布)：%d" % b)
#     if (a == 3 and b == 1 or a == 2 and b == 3 or a == 1 and b == 2):
#         print("玩家获胜")
#     elif (a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3):
#         print("平局")
#     else:
#         print("电脑获胜")

# while 1:
#     a = str(input("你喜欢谁："))
#     if a == "邓紫棋":
#         print("你真优秀")
#     else:
#         print("呸，你这个垃圾，你应该喜欢邓紫棋")
# i = 1
# a = 0
# while i <= 100:
#     a = a + i`
#     i = i + 1
# print(a)

# a = 1
# while a <= 9:
#     c = 1
#     while c <= a:
#         print("%d * %d = %d" % (c,a,a*c,),end="\t")
#         c += 1
#     print("")

    # a += 1

# a = 2
# b = 0
# while a <= 100:
#     if a % 2 != 0 and a % 3 != 0 and a % 7 != 0 and a % 5 != 0 :
#         b = b + a
#         print(a)
#     a += 1
# b = b + 2 + 3 + 7 + 5
# print(b)











# a = 2
# c = 0
# while a <= 100:
#     b = 2
#     while b < a:
#       if a % b == 0:
#           break
#
#       b = b + 1
#     else:
#         c += a
#     a = a + 1
# print(c)

